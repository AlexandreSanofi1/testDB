import boto3
from datetime import datetime
import time

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

# Reference the table name
table_name = 'testIndexPerf'

# Record the start time
start_time = time.time()

# List to hold the batch of items
batch_items = []

print(f"Inserting 10,000 lines in batches of 25\n")

# Loop to create 10,000 items to insert into the DynamoDB table
for i in range(1, 10001):
    # Construct the item
    item = {
        'TestID': {'S': str(i)},  # Unique identifier (partition key)
        'AttributeName': {'S': f'SampleAttribute{i}'},  # Example of dynamic attribute
        'TimeStamp': {'S': str(datetime.now())}  # Current timestamp
    }

    # Append the item to the batch
    batch_items.append({
        'PutRequest': {
            'Item': item
        }
    })

    # Insert in batches of 25 items (DynamoDB allows a max of 25 items per batch)
    if len(batch_items) == 25:
        # Use batch_write_item to insert the items
        response = dynamodb.batch_write_item(
            RequestItems={
                table_name: batch_items
            }
        )
        print(f'{i} items written to DynamoDB.')
        batch_items = []  # Clear the list after each batch

        # Add a delay between batch requests (start with 0.1 seconds and adjust if necessary)
        time.sleep(0.5)  # 500ms delay

# Insert any remaining items that weren't inserted in the last batch
if batch_items:
    dynamodb.batch_write_item(
        RequestItems={
            table_name: batch_items
        }
    )
    print(f'{len(batch_items)} remaining items written to DynamoDB.')

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
print(f"Total time taken to insert 10,000 items: {total_time:.2f} seconds")


"""
9550 items written to DynamoDB.
9575 items written to DynamoDB.
9600 items written to DynamoDB.
9625 items written to DynamoDB.
9650 items written to DynamoDB.
9675 items written to DynamoDB.
9700 items written to DynamoDB.
9725 items written to DynamoDB.
9750 items written to DynamoDB.
9775 items written to DynamoDB.
9800 items written to DynamoDB.
9825 items written to DynamoDB.
9850 items written to DynamoDB.
9875 items written to DynamoDB.
9900 items written to DynamoDB.
9925 items written to DynamoDB.
9950 items written to DynamoDB.
9975 items written to DynamoDB.
10000 items written to DynamoDB.
Start time: 2024-09-13 14:53:35
End time: 2024-09-13 15:07:11
Total time taken to insert 1000 items: 815.81 seconds
"""


"""
How Throttling Works
Capacity Unit Calculations:

1 WCU: Allows one write per second for an item up to 1KB in size.
1 RCU: Allows two reads per second (eventually consistent) or one strongly consistent read for an item up to 4KB in size.
"""
