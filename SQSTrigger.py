import boto3
sqs = boto3.client("sqs")
queue_url = "INSERTQUEUEURLHERE"
response = sqs.send_message(
    QueueUrl = queue_url,
    DelaySeconds = 10,
    MessageAttributes={
        "Body": "SQS Message Sent"
    },
    MessageBody=("SQS ping to Lambda")
)
print(response["MessageID"])