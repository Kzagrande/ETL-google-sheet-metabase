import json
from logs import log
from googleSheetAuth import main

def lambda_handler(event, context):
    main()         
    log('event' + json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
