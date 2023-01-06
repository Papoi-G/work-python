from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive' ]

SPREADSHEET_ID = '1-ohi3MJU2Y6inrEa2-8XiI7-Bb_G1q-J0_aYSQTh5nw'
RANGE_NAME_1 = 'Event Marketing Timeline!B10:H12'
RANGE_NAME_2 = 'copy format!A1:G'

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
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()   
        requests = []
        obj = sheet.get(spreadsheetId=SPREADSHEET_ID, ranges=RANGE_NAME_1, fields='sheets(data(rowData(values(userEnteredFormat))),properties(sheetId))').execute()

        body = {
            'requests': requests }
        response = service.spreadsheets().batchUpdate(
            spreadsheetId=SPREADSHEET_ID,
            body=body).execute()
        find_replace_response = response.get('replies')[1].get('findReplace')
        print('{0} replacements made.'.format(
            find_replace_response.get('occurrencesChanged')))
        return response

        {
            "requests": [
                {
                "copyPaste": {
                    "source": {
                    "sheetId": SPREADSHEET_ID,
                    "startRowIndex": 0,
                    "endRowIndex": 7,
                    "startColumnIndex": 0,
                    "endColumnIndex": 4
                    },
                    "destination": {
                    "sheetId": SPREADSHEET_ID,
                    "startRowIndex": 0,
                    "endRowIndex": 10,
                    "startColumnIndex": 5,
                    "endColumnIndex": 9
                    },
                    "pasteType": "PASTE_FORMAT",
                    "pasteOrientation": "NORMAL"
                }
                }
            ]
        }

    

        
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()