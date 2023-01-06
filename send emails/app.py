from __future__ import print_function

import base64
from email.message import EmailMessage

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account



def gmail_send_message():
    """Create and send an email message
    Print the returned  message id
    Returns: Message object, including message id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    SCOPES = ['https://mail.google.com/']
    SERVICE_ACCOUNT_FILE = 'serviceaccount.json'

    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,
            scopes=SCOPES,
            subject='valladaresk@support-domain11.xyz')

    try:
        service = build('gmail', 'v1', credentials=credentials)
        message = EmailMessage()

        message.set_content('This is automated draft mail, to test services accounts impersonations')

        message['To'] = 'kvalladares@support-domain30.xyz'
        message['From'] = 'valladaresk@support-domain11.xyz'
        message['Subject'] = 'Automated draft'

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()

        create_message = {
            'raw': encoded_message
        }
        # pylint: disable=E1101
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message


if __name__ == '__main__':
    gmail_send_message()