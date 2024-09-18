import boto3
import time

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

# Reference the table name
table_name = 'test30Indexes'

def scan_with_filters():
    print("Scanning with filters...")
    total_items_found = 0
    start_time = time.time()

    try:
        response = dynamodb.scan(
            TableName=table_name,
            FilterExpression='GSI_Attribute_1 > :gsi1 AND GSI_Attribute_2 > :gsi2 AND GSI_Attribute_3 > :gsi3 AND GSI_Attribute_8 > :gsi8 AND GSI_Attribute_9 > :gsi9',
            ExpressionAttributeValues={
                ':gsi1': {'N': '978'},
                ':gsi2': {'N': '977'},
                ':gsi3': {'N': '999'},
                ':gsi8': {'N': '980'},
                ':gsi9': {'N': '999'},
            }
        )

        # Count the items found
        items = response.get('Items', [])
        #print(items)
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
