import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

# Add a Global Secondary Index to an existing table
response = dynamodb.update_table(
    TableName='test30Indexes',
    AttributeDefinitions=[
        {
            'AttributeName': 'NewAttribute',
            'AttributeType': 'S'
        },
    ],
    GlobalSecondaryIndexUpdates=[
        {
            'Create': {
                'IndexName': 'index21',
                'KeySchema': [
                    {
                        'AttributeName': 'NewAttribute',
                        'KeyType': 'HASH'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'  # Choose between KEYS_ONLY, INCLUDE, or ALL
                }
                # Remove the ProvisionedThroughput parameter for PAY_PER_REQUEST tables
            }
        }
    ]
)

print(response)

