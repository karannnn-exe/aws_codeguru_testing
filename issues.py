import json
import boto3

def lambda_handler(event, context):
    # Example of hardcoded values, inefficient use of resources, and potential security issues
    s3 = boto3.client('s3')
    
    # Hardcoded bucket name (security issue)
    bucket_name = 'my-example-bucket'
    
    # Inefficient handling of a large S3 object (performance issue)
    try:
        response = s3.get_object(Bucket=bucket_name, Key='large-file.txt')
        data = response['Body'].read()  # Reading the entire file into memory (inefficient)
        
        # Inefficient and insecure way to process data
        lines = data.decode('utf-8').split('\n')
        for line in lines:
            print(line)  # Printing each line, which can be slow and insecure if the log is exposed
        
        return {
            'statusCode': 200,
            'body': json.dumps('File processed successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing file: {}'.format(e))
        }

# Note: This code has several issues that AWS CodeGuru should flag:
# - Hardcoded S3 bucket name, which is a security risk.
# - Inefficient handling of large files by reading the entire file into memory.
# - Inefficient logging method by printing each line individually.
# - Lack of proper error handling and resource management.
