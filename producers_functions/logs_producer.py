import boto3
import pandas as pd
import random

s3 = boto3.client("s3")

BUCKET = "ecommerce-analytics-lake-ishwar"

events = [
    "LOGIN",
    "SEARCH",
    "ERROR",
    "CHECKOUT"
]

for country in ["india","uk","canada"]:

    rows = []

    for i in range(1):

        rows.append({
            "log_id": i,
            "event_type": random.choice(events),
            "user_id": f"U{random.randint(1,500)}",
            "country": country
        })

    df = pd.DataFrame(rows)

    filename = f"logs_{country}.csv"

    df.to_csv(
        filename,
        index=False
    )

    s3.upload_file(
        filename,
        BUCKET,
        f"raw/{country}/logs/{filename}"
    )

print("Logs uploaded")