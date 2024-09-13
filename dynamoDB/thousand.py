import boto3
from datetime import datetime
import time

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Reference the test table
table = dynamodb.Table('testIndexPerf')

# Loop to insert 1000 items into the table
for i in range(1, 1001):
    # Construct the item
    item = {
        'TestID': str(i),  # Unique partition key (TestID 1 to 1000)
        'AttributeName': f'SampleAttribute{i}',  # Example of dynamic attribute
        'TimeStamp': str(datetime.now())  # Current timestamp
    }

    # Insert the item into the table
    response = table.put_item(Item=item)

    # Print progress every 100 items
    if i % 100 == 0:
        print(f'{i} items written to DynamoDB.')

    # Optional: Add a small delay to avoid throttling
    time.sleep(0.01)  # 10ms delay to prevent overwhelming the table

print("Finished inserting 1000 items.")
