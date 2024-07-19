import json
import boto3
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize the Boto3 client at the module level
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get the bucket name and key from the event or environment variables
    bucket_name = event.get('bucket_name', 'my-example-bucket')
    key = event.get('key', 'large-file.txt')
    
    try:
        # Fetch the object from S3
        response = s3.get_object(Bucket=bucket_name, Key=key)
        data = response['Body'].iter_lines()  # Use iter_lines to handle large files efficiently

        # Process the data securely
        for line in data:
            decoded_line = line.decode('utf-8')
            logger.info(decoded_line)  # Use logger instead of print for secure logging

        return {
            'statusCode': 200,
            'body': json.dumps('File processed successfully!')
        }
    except Exception as e:
        logger.error('Error processing file: %s', e)
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error processing file: {str(e)}')
        }
