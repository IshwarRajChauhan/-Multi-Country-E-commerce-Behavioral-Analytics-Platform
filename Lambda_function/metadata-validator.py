import boto3

glue = boto3.client("glue")

def lambda_handler(event, context):

    for record in event["Records"]:

        key = record["s3"]["object"]["key"]

        print(f"New file uploaded: {key}")

        if "/orders/" in key:

            response = glue.start_workflow_run(
                Name="orders_workflow"
            )

            print(
                f"Started orders_workflow: {response['RunId']}"
            )

        elif "/logs/" in key:

            response = glue.start_workflow_run(
                Name="logs_workflow"
            )

            print(
                f"Started logs_workflow: {response['RunId']}"
            )

        elif "/clickstream/" in key:

            response = glue.start_workflow_run(
                Name="clickstream_workflow"
            )

            print(
                f"Started clickstream_workflow: {response['RunId']}"
            )

    return {
        "statusCode": 200
    }