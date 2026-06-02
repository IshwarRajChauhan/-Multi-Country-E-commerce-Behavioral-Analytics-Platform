import boto3
import pandas as pd
import random

s3 = boto3.client("s3")

BUCKET = "ecommerce-analytics-lake-ishwar"

for country in ["india","uk","canada"]:

    rows = []

    for i in range(1):

        rows.append({
            "order_id": random.randint(10000,99999),
            "user_id": f"U{random.randint(1,500)}",
            "amount": random.randint(100,5000),
            "country": country
        })

    df = pd.DataFrame(rows)

    filename = f"orders_{country}.csv"

    df.to_csv(
        filename,
        index=False
    )

    s3.upload_file(
        filename,
        BUCKET,
        f"raw/{country}/orders/{filename}"
    )

print("Orders uploaded")