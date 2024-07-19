import json
import boto3

# Hardcoded AWS credentials (for demonstration purposes only)
AWS_ACCESS_KEY_ID = 'AKIAR4NKES2I'
AWS_SECRET_ACCESS_KEY = 'PoUgeoA8/WRPq8UD+a/ESR61'

# Initialize the Boto3 client at the module level
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def lambda_handler(event, context):
    # Example of hardcoded values, inefficient use of resources, and potential security issues
    bucket_name = 'my-example-bucket'
    
    try:
        response = s3.get_object(Bucket=bucket_name, Key='large-file.txt')
        data = response['Body'].read()  
        
        lines = data.decode('utf-8').split('\n')
        for line in lines:
            print(line) 
        
        return {
            'statusCode': 200,
            'body': json.dumps('File processed successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing file: {}'.format(e))
        }
