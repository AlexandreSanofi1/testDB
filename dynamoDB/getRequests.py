import boto3
import time

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

# Reference the table name
table_name = 'test30Indexes'

# Function to perform a GetItem operation
def get_item_test():
    print("Performing GetItem test...")
    start_time = time.time()
    try:
        # Replace with an actual 'TestID' and 'TimeStamp' that exists in your table
        response = dynamodb.get_item(
            TableName=table_name,
            Key={
                'TestID': {'S': '1'},
                'TimeStamp': {'S': '2024-09-17 18:09:56.545948'}  # Replace with an actual timestamp
            }
        )
        print("Item retrieved:", response.get('Item', 'No item found'))
    except Exception as e:
        print(f"Error during GetItem: {e}")
    end_time = time.time()
    print(f"GetItem test completed in {end_time - start_time:.2f} seconds.\n")

# Function to perform a Query operation on the primary key
def query_test():
    print("Performing Query test on primary key...")
    start_time = time.time()
    try:
        response = dynamodb.query(
            TableName=table_name,
            KeyConditionExpression='#d = :test_id',
            ExpressionAttributeNames={
                '#d': 'TestID'
            },
            ExpressionAttributeValues={
                ':test_id': {'S': '1'}  # Replace with a value that exists in your table
            }
        )
        print("Items found:", len(response.get('Items', [])))
    except Exception as e:
        print(f"Error during Query: {e}")
    end_time = time.time()
    print(f"Query test completed in {end_time - start_time:.2f} seconds.\n")

# Function to perform a Query operation on a Global Secondary Index (GSI)
def query_gsi_test():
    print("Performing Query test on GSI...")
    start_time = time.time()
    try:
        response = dynamodb.query(
            TableName=table_name,
            IndexName='index2',  # Replace with one of the correct GSI names like 'index10'
            KeyConditionExpression='TestID = :test_id',
            ExpressionAttributeValues={
                ':test_id': {'S': '1'}  # Replace with a value that matches the GSI key
            }
        )
        print("Items found in GSI query:", len(response.get('Items', [])))
    except Exception as e:
        print(f"Error during GSI Query: {e}")
    end_time = time.time()
    print(f"GSI Query test completed in {end_time - start_time:.2f} seconds.\n")

# Function to perform a Scan operation (use sparingly for large tables)
def scan_test():
    print("Performing Scan test...")
    start_time = time.time()
    try:
        response = dynamodb.scan(
            TableName=table_name,
        )
        print("Total items scanned:", len(response.get('Items', [])))
    except Exception as e:
        print(f"Error during Scan: {e}")
    end_time = time.time()
    print(f"Scan test completed in {end_time - start_time:.2f} seconds.\n")

# Run the read tests
get_item_test()
query_test()
query_gsi_test()
scan_test()
