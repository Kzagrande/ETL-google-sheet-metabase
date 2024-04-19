from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import pandas as pd
import logging

# Configurando o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

        logger.info("Dados extraídos com sucesso do Google Sheets.")

        # Convert values to DataFrame
        if values:
            df = pd.DataFrame(values[1:], columns=values[0])
            logger.info("Valores convertidos em DataFrame com sucesso.")
            return df
        else:
            logger.warning("Nenhum dado encontrado.")
            return None

    except HttpError as err:
        logger.error(f"Erro ao extrair dados do Google Sheets: {err}")
        print(err)

# if __name__ == "__main__":
#   google_sheet_extractive()
