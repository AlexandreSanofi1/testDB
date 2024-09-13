import boto3

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Reference the test table
table = dynamodb.Table('testIndexPerf')

# Scan the table to retrieve all items
response = table.scan()

# Get the items from the response
items = response.get('Items', [])

# Print the items
if items:
    print("Items in the table:")
    for item in items:
        print(item)
else:
    print("No items found in the table.")
