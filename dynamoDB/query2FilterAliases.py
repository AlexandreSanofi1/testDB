import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

# Reference the table name
table_name = 'test30Indexes'

def query_with_filters():
    print("Querying with filters...")
    try:
        # Perform the query operation
        response = dynamodb.query(
            TableName=table_name,
            KeyConditionExpression='TestID = :test_id AND #ts > :timestamp_val',
            FilterExpression='GSI_Attribute_1 = :gsi1 AND GSI_Attribute_2 > :gsi2',
            ExpressionAttributeNames={
                '#ts': 'TimeStamp'  # Alias for the reserved keyword
            },
            ExpressionAttributeValues={
                ':test_id': {'S': '9990'},
                ':timestamp_val': {'S': '2024-09-15 18:15:17.140429'},
                ':gsi1': {'S': 'Value_1_9990'},
                ':gsi2': {'S': '0'}
            },
            ScanIndexForward=False  # To sort in descending order
        )

        # Print the items found
        items = response.get('Items', [])
        print(f"Items found: {len(items)}")
        for item in items:
            print(item)

    except Exception as e:
        print(f"Error during query with filters: {e}")

# Run the query with filters
query_with_filters()
