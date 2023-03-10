from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import email
import base64 #add Base64
import time 

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            
        #Filter and gets the IDs of the message I need. 
        #I'm just filtering messages that have the word 'Rule triggered' inside my Inbox

    try:
        service = build('gmail', 'v1', credentials=creds)
        search_id = service.users().messages().list(userId='me', q = 'alert').execute()
        number_result = search_id['resultSizeEstimate']

        final_list = [] # empty array, all the messages ID will be listed here
        
        # review if the search is empty or not
        # if it has messages on it, It will enter the for

        if number_result>0:
            message_ids = search_id['messages']

            for ids in message_ids:
                final_list.append(ids['id'])
                # call the funtion that will call the body of the message
                get_message(service, ids['id'] )
                
            return final_list
        
        # If there are not messages with those criterias 
        #The message 'There were 0 results for that search string' will be printed. 

        else:
            print('There were 0 results for that search string')
            return ""

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')
        
        
        #new funtion to get the body of the message, and decode the message

def get_message(service, msg_id):

    try:
        message_list=service.users().messages().get(userId='me', id=msg_id, format='raw').execute()

        msg_raw = base64.urlsafe_b64decode(message_list['raw'].encode('ASCII'))

        msg_str = email.message_from_bytes(msg_raw)

        content_types = msg_str.get_content_maintype()
        
        #how it will work when is a multipart or plain text

        if content_types == 'multipart':
            part1, part2 = msg_str.get_payload()
            print("This is the message body, html:")
            print(part1.get_payload())
            return part1.get_payload()
        else:
            print("This is the message body plain text:")
            print(msg_str.get_payload())
            return msg_str.get_payload()


    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()