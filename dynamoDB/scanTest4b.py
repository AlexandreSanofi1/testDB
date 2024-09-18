import boto3
import time

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

# Reference the table name
table_name = 'test4'

def scan_with_filters():
    print("Scanning with filters...")
    total_items_found = 0
    start_time = time.time()

    try:
        response = dynamodb.scan(
            TableName=table_name,
            FilterExpression='GSI_Attribute_1 > :gsi1',
            ExpressionAttributeValues={
                ':gsi1': {'N': '50000'},
            }
        )

        # Count the items found
        items = response.get('Items', [])
        total_items_found += len(items)

    except Exception as e:
        print(f"Error during scan with filters: {e}")

    end_time = time.time()

    # Calculate the total time taken
    total_time = end_time - start_time

    # Report results
    print(f"Total items found: {total_items_found}")
    print(f"Total time taken for scan: {total_time:.2f} seconds")

# Run the scan with filters
scan_with_filters()


"""
Total time taken to insert 10,000 items: 263.86 seconds
(venv) alleonet@Alexandres-MBP dynamoDB % python3 scanTest4b.py 
Scanning with filters...
Total items found: 11290
Total time taken for scan: 2.02 seconds
(venv) alleonet@Alexandres-MBP dynamoDB % python3 scanTest4b.py
Scanning with filters...
Total items found: 11290
Total time taken for scan: 2.77 seconds
(venv) alleonet@Alexandres-MBP dynamoDB % python3 scanTest4b.py
Scanning with filters...
Total items found: 5687
Total time taken for scan: 1.21 seconds

"""
