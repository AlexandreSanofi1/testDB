import boto3
import time

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

# Reference the table name
table_name = 'test30Indexes'

def query_with_filters():
    print("Querying 1,000 different keys with filters...")
    total_items_found = 0
    start_time = time.time()

    for i in range(1, 1001):  # Query 1000 different keys
        try:
            # Perform the query operation
            response = dynamodb.query(
                TableName=table_name,
                KeyConditionExpression='TestID = :test_id AND #ts > :timestamp_val',
                FilterExpression='GSI_Attribute_1 = :gsi1 AND GSI_Attribute_2 > :gsi2 AND GSI_Attribute_3 > :gsi3 AND GSI_Attribute_8 > :gsi8 AND GSI_Attribute_9 > :gsi9',
                ExpressionAttributeNames={
                    '#ts': 'TimeStamp'  # Alias for the reserved keyword
                },
                ExpressionAttributeValues={
                    ':test_id': {'S': str(7770 + i)},  # Use different TestID values
                    ':timestamp_val': {'S': '2024-09-15 18:15:17.140429'},
                    ':gsi1': {'S': f'Value_1_{7770 + i}'},
                    ':gsi2': {'S': '0'},
                    ':gsi3': {'S': '0'},
                    ':gsi8': {'S': '0'},
                    ':gsi9': {'S': '0'},
                },
                ScanIndexForward=False  # To sort in descending order
            )

            # Count the items found in each query
            items = response.get('Items', [])
            print(items)
            total_items_found += len(items)

        except Exception as e:
            print(f"Error during query with filters for TestID {9990 + i}: {e}")

    end_time = time.time()

    # Calculate the total time taken
    total_time = end_time - start_time
    average_time_per_query = total_time / 1000

    # Report results
    print(f"Total items found: {total_items_found}")
    print(f"Total time taken for 1000 queries: {total_time:.2f} seconds")
    print(f"Average time per query: {average_time_per_query:.4f} seconds")

# Run the read speed test
query_with_filters()



"""

test :
Find all where the TestID is equal to a specific value and the TimeStamp is greater than a given timestamp.
Further filter  where GSI_Attribute_1 == value1 AND and GSI_Attribute_2 > 0.

#querying with 2 filters.Ò
(venv) alleonet@Alexandres-MBP dynamoDB % python3 read1000Lines.py 
Querying 1,000 different keys with filters...
Total items found: 10
Total time taken for 1000 queries: 108.88 seconds
Average time per query: 0.1089 seconds

#querying with 2 filters
(venv) alleonet@Alexandres-MBP dynamoDB % python3 read1000Lines.py 
Total items found: 1000
Total time taken for 1000 queries: 109.36 seconds
Average time per query: 0.1094 seconds

#querying with 3 filters
Total items found: 1000
Total time taken for 1000 queries: 56.91 seconds
Average time per query: 0.0569 seconds

# querying with 5 filters
Total items found: 1000
Total time taken for 1000 queries: 61.51 seconds
Average time per query: 0.0615 seconds

(venv) alleonet@Alexandres-MBP dynamoDB % 
"""


