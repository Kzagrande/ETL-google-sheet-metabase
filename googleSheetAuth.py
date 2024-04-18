from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

# If modifying these scopes, update the list accordingly
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet
SAMPLE_SPREADSHEET_ID = "1Fo4-kMbFJ9JUauGmQFo97fU9YiHrO1jn1zRCybXdYRg"
SAMPLE_RANGE_NAME = "UPH per Process!A:K"

def google_sheet_main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # Path to your service account JSON file
    SERVICE_ACCOUNT_FILE = 'C:/Users/casag/sites/lambda-rpa-uph/my_service_account_credentials.json'

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        print("Name, Major:")
        for row in values:
            print(f"{row[0]}, {row[4]}")
    except HttpError as err:
        print(err)

