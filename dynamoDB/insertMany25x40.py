import boto3
from datetime import datetime
import time

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Reference the test table (Replace 'testIndexPerf' with your table name)
table = dynamodb.Table('testIndexPerf')

# Record the start time
start_time = time.time()

# List to hold the batch of items
items = []

# Loop to create 1000 items to insert into the DynamoDB table
for i in range(1, 1001):
    # Construct the item
    item = {
        'TestID': str(i),  # Unique identifier (partition key)
        'AttributeName': f'SampleAttribute{i}',  # Example of dynamic attribute
        'TimeStamp': str(datetime.now())  # Current timestamp
    }

    # Append the item to the batch
    items.append({
        'PutRequest': {
            'Item': item
        }
    })

    # Insert in batches of 25 items (DynamoDB allows a max of 25 items per batch)
    if len(items) == 25:
        # Use batch_write_item to insert the items
        with table.batch_writer() as batch:
            for item in items:
                batch.put_item(Item=item['PutRequest']['Item'])
        print(f'{i} items written to DynamoDB.')
        items = []  # Clear the list after each batch

# Insert any remaining items that weren't inserted in the last batch (if total count isn't a multiple of 25)
if items:
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item['PutRequest']['Item'])
    print(f'{len(items)} remaining items written to DynamoDB.')

# Record the end time
end_time = time.time()

# Calculate the total time taken
total_time = end_time - start_time

# Convert start and end time to human-readable format
start_time_readable = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
end_time_readable = datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')

# Print the start time, end time, and total time
print(f"Start time: {start_time_readable}")
print(f"End time: {end_time_readable}")
print(f"Total time taken to insert 1000 items: {total_time:.2f} seconds")
