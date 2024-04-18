import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import json
import pandas as pd

# If modifying these scopes, update the list accordingly
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet
SAMPLE_SPREADSHEET_ID = "1Fo4-kMbFJ9JUauGmQFo97fU9YiHrO1jn1zRCybXdYRg"
SAMPLE_RANGE_NAME = "UPH per Process!A:K"

def google_sheet_extractive():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    # ------------- LOCAL ----------------
    # SERVICE_ACCOUNT_FILE = 'C:/Users/casag/sites/lambda-rpa-uph/my_service_account_credentials.json'
    # creds = service_account.Credentials.from_service_account_file(
    #     SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    

    # ---------- LAMBDA ----------------
    service_account_json = os.getenv('GOOGLE_SERVICE_ACCOUNT_JSON')
    creds_dict = json.loads(service_account_json)
    creds = service_account.Credentials.from_service_account_info(creds_dict, scopes=SCOPES)

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

                # Convert values to DataFrame
        if values:
            df = pd.DataFrame(values[1:], columns=values[0])
            # print('df',df)
            return df
        else:
            print("No data found.")
            return None

    except HttpError as err:
        print(err)

# if __name__ == "__main__":
#   google_sheet_extractive()