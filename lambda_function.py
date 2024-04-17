import json
from logs import log

def lambda_handler(event, context):
    # TODO implement
    log('Log de execução. event:' + json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
