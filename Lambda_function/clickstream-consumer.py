import json
import boto3
import base64

s3 = boto3.client("s3")

BUCKET = "ecommerce-analytics-lake-ishwar"

def lambda_handler(event, context):

    for record in event["Records"]:

        payload = json.loads(
            base64.b64decode(
                record["kinesis"]["data"]
            )
        )

        country = payload["country"]

        key = (
            f"raw/{country}/clickstream/"
            f"{payload['timestamp']}.json"
        )

        s3.put_object(
            Bucket=BUCKET,
            Key=key,
            Body=json.dumps(payload)
        )

    return {
        "statusCode": 200
    }