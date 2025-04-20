import json

def lambda_handler(event, context):
    name = event.get('queryStringParameters', {}).get('name', 'World')
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Hello, {name}!'}),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
