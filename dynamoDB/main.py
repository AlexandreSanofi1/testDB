import boto3
from datetime import datetime

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Reference the test table
table = dynamodb.Table('testIndexPerf')

# Insert an item into the table
response = table.put_item(
   Item={
        'TestID': '123',  # Partition key
        'AttributeName': 'SampleAttribute',  # Additional attribute
        'TimeStamp': str(datetime.now()),  # Example of dynamic timestamp
    }
)

# Print the response
print(response)
