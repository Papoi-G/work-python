import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.oauth2 import service_account


def main():
    SCOPES = ['https://www.googleapis.com/auth/apps.alerts']
    SERVICE_ACCOUNT_FILE = 'serviceaccount.json'

    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,
            scopes=SCOPES,
            subject='jc@jklav.com')
            
    #delegated_credentials = credentials.with_subject('user@domain.com')      

    service = build('alertcenter', 'v1beta1', credentials=credentials)

    query = service.alerts().list().execute()

    print(query)

if __name__ == '__main__':
    main()