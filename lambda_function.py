import json
from logs import log

def lambda_handler(event, context):
    # TODO implement
    log('event' + json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
