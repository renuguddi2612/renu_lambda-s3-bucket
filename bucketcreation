import boto3

def lambda_handler(event, context):

    s3 = boto3.client('s3')

    bucket_name = "my-github-actions-bucket-12345"

    s3.create_bucket(
        Bucket=bucket_name
    )

    return {
        'statusCode': 200,
        'body': f'Bucket {bucket_name} created successfully'
    }