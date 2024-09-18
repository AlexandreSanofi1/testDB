import boto3
from datetime import datetime
import time

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

# Reference the table name
table_name = 'test4'

# Record the start time
start_time = time.time()

# List to hold the batch of items
batch_items = []

print(f"Inserting 10,000 lines in batches of 25\n")

# Loop to create 10,000 items to insert into the DynamoDB table
for i in range(1, 100001):
    # Construct the item with attributes corresponding to each index
    
    item = {
        'TestID': {'S': str(i)},  # Unique identifier (partition key)
        'TimeStamp': {'S': str(datetime.now())},  # Current timestamp
        'AttributeName': {'S': f'SampleAttribute'},  # Example of dynamic attribute
        # Add attributes for each GSI
        #**{f'GSI_Attribute_{j}': {'S': f'Value_{j}_{i}'} for j in range(1, 21)}
        **{f'GSI_Attribute_{j}': {'N': str(i)} for j in range(1, 2)}

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
        # Uncomment if you experience throttling
        # time.sleep(0.1)  # 100ms delay

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
results :
9975 items written to DynamoDB.
10000 items written to DynamoDB.
Start time: 2024-09-17 18:13:56
End time: 2024-09-17 18:15:17
Total time taken to insert 10,000 items: 80.90 seconds

"""
