import boto3

def lambda_handler(event, context):

    s3 = boto3.client('s3')

    bucket_name = "renu-github-actions-bucket-123"

    s3.create_bucket(
        Bucket=bucket_name
    )

    return {
        "statusCode": 200,
        "body": "Bucket created successfully"
    }