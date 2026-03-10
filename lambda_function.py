import boto3

def lambda_handler(event, context):

    s3 = boto3.client('s3')

    bucket_name = "renu-github-actions-bucket-123"

    s3.create_bucket(
        Bucket=bucket_name
    )

    print "this is for creating s3 bucket"

    return {
        "statusCode": 200,
        "body": "Bucket created successfully"
    }