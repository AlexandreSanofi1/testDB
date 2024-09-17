import boto3
from datetime import datetime
import time

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Reference the test table
table = dynamodb.Table('test30Indexes')

# Record the start time
start_time = time.time()

# Use batch_writer to handle batch inserts automatically
with table.batch_writer() as batch:
    # Loop to create 1000 items to insert into the DynamoDB table
    for i in range(1, 1001):
        # Construct the item with attributes corresponding to each index
        item = {
            'TestID': str(i),  # Unique identifier (partition key)
            'TimeStamp': str(datetime.now()),  # Current timestamp
            # Adding attributes for each index
            **{f'GSI_Attribute_{j}': f'Value_{j}_{i}' for j in range(1, 21)}
        }

        # Add item to the batch
        batch.put_item(Item=item)

        # Optional: print progress for every 100 items
        if i % 100 == 0:
            print(f'{i} items added to the batch.')

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
