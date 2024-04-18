import json
from logs import log
from googleSheetAuth import google_sheet_main

def lambda_handler(event, context):
    google_sheet_main()         
    log('event' + json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
