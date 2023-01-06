# impor this libraries that you will use for the calendar API

from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# The scopes that we need to use based on the Google documentation
# I added the information in the reference at the end of the answer

SCOPES = ['https://www.googleapis.com/auth/calendar', 
        'https://www.googleapis.com/auth/calendar.events']

# creation of the credential, I use as a base the Google Documentation "Python quickstart"

def main():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # The list of people that will be use in each event 
        peoples = ['Person 1', 'Person 2', 'Person 3', 'Person 4']
        number_week = 0

        event = {
            # Event title
            'summary': 'Testing create description',
            # A test description, this will be replace later, so you can add anything you want on it. 
            'description': 'test',
            # The start and end date need to be in ISO-8601 date format
            # and the time zone needs to be formatted as an IANA Time Zone Database name, e.g. "Europe/Zurich 
            'start': {
                'dateTime': '2022-10-28T09:00:00-07:00',
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': '2022-10-28T17:00:00-07:00',
                'timeZone': 'America/Los_Angeles',
            },
            'recurrence': [
            # You can change the recurrency of the event 
            # for this example is a weekly event, and it has 4 recurrencies
                'RRULE:FREQ=WEEKLY;COUNT=8'
            ],
            # The list of attendees
            'attendees': [
                {'email': 'test@email.xyz'},
                {'email': 'test2@email.xyz'},
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
                ],
            },
            }

        # We use insert to create the event
        event = service.events().insert(calendarId='primary', body=event).execute()
        # You can use the print in the next line to see the information of the event while you are testing
        # print('Event created: %s' % (event.get('htmlLink')))
        page_token = None

        # Search for the event, using method list and the event title q='Testing create description'
        # you can use any other search key to get the event ID
        events = service.events().list(calendarId='primary', pageToken=page_token, q='Testing create description').execute()  
              
        # get the ID of the event
        for event in events['items']:
            print(event['id'])
            id_event = event['id']


            # Will search the ID of the recurrencies of the event using the method instances 
            # e.g. xxxxxxxxxxxxxxxxx_20221028T160000Z                    
            while True:
                recurrences_for_events = service.events().instances(calendarId='primary', eventId=id_event,
                                      pageToken=page_token).execute()

                # run the dictionary of each iteration     
                for recurrence_instance in recurrences_for_events['items']:
                    id_to_update = recurrence_instance['id']
                    # I used the next print just to review the IDs of each event
                    # print(id_to_update)

                    # Create the new body of the event with name of the people in the list peoples
                    # instead of using year, week, day = datetime.date.today().isocalendar(). I use a simple counter to iterate on the list
                    body = {
                        'description': peoples[number_week],                        
                    }
                    # update the event description with patch
                    updated_event = service.events().patch(calendarId='primary', eventId=id_to_update, body=body).execute()
                    print(updated_event['description'])
                    # next patch in case you have a large recrrency of the event
                    page_token = events.get('nextPageToken')
                    number_week += 1

                    # This if will reset the counter, in case the number of people is less than the recurrencies of the event
                    if number_week >= len(peoples):
                        number_week = 0

                if not page_token:
                    break
            

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()