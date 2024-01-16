import json

def lambda_handler(event, context):
    # TODO: Implement your logic here
    print(json.dumps(event))  # Use json.dumps to pretty print the event

    try:
        for record in event['Records']:
            s3_event = json.loads(record['body'])
            
            if 'Event' in s3_event and s3_event['Event'] == 's3:TestEvent':
                print("Test Event")
            else:
                for s3_record in s3_event.get('Records', []):
                    print("Bucket Name: {}".format(s3_record['s3']['bucket']['name']))
                    print("Object Key: {}".format(s3_record['s3']['object']['key']))
                    
    except Exception as e:
        print("Exception: {}".format(e))
