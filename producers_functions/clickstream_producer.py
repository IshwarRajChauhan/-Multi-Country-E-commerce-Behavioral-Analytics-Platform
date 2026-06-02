import boto3
import json
import random
import time
from datetime import datetime

kinesis = boto3.client(
    "kinesis",
    region_name="ap-south-1"
)

STREAM_NAME = "clickstream-stream"

countries = [
    "india",
    "uk",
    "canada"
]

pages = [
    "home",
    "search",
    "product",
    "cart",
    "checkout"
]

n=1
while n > 0:

    event = {
        "user_id": f"U{random.randint(1000,9999)}",
        "country": random.choice(countries),
        "page": random.choice(pages),
        "timestamp": datetime.utcnow().isoformat()
    }

    kinesis.put_record(
        StreamName=STREAM_NAME,
        Data=json.dumps(event),
        PartitionKey=event["user_id"]
    )

    print(event)

    time.sleep(2)
    n -= 1