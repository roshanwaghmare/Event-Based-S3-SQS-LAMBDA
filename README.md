# Event-Based-S3-SQS-LAMBDA
The main purpose of this is to simulate a small portion of an event-based project which is very frequently used by many companies.


![Uploading image.png…]()


First we create S3 Bucket and folder inside
then will create SQS queue and create genrate one new policy for our S3

Amazon SQS
Queues
sqsforlambda
Edit
Policy generator

craete policy as below

```
{
  "Id": "Policy1705391989090",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1705391960147",
      "Action": "sqs:*",
      "Effect": "Allow",
      "Resource": "arn:aws:sqs:us-east-1:688646276098:sqsforlambda",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:s3:::demos3sqs79"
        }
      },
      "Principal": "*"
    }
  ]
}
```



Amazon S3/ Buckets/ Properties/ Event Notification

create event will select all put /post/copy
select SQS select our queue
save 

create Lambda Function

selct Python 3.9 save

LAMBDA CODE BELOW

````
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


````
go to permission create role SQS full access 

now ADD file in S3 bucket and inside folder as well
now will add trigger so 
select SQS 
batch size 1
batch window 10
SAVE 

now go to SQS you will find 
Messages available will be 0
Messages in flight will be 0

now go back to lambda and go to Monitor /View CloudWatch logs u will be directed to cloud watch logs u can check log in records copy that record serch json formatter and view the records 
