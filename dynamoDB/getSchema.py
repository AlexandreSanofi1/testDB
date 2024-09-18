import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

# Table name
table_name = 'test30Indexes'  # Replace with your table name

def get_table_schema():
    try:
        # Get the table description
        response = dynamodb.describe_table(TableName=table_name)
        table_description = response['Table']

        # Print the table schema details
        print("Table Name:", table_description['TableName'])
        print("Attribute Definitions:")
        for attribute in table_description['AttributeDefinitions']:
            print(f"  - {attribute['AttributeName']}: {attribute['AttributeType']}")

        print("\nKey Schema:")
        for key in table_description['KeySchema']:
            print(f"  - {key['AttributeName']}: {key['KeyType']}")

        # List Global Secondary Indexes (if any)
        if 'GlobalSecondaryIndexes' in table_description:
            print("\nGlobal Secondary Indexes:")
            for gsi in table_description['GlobalSecondaryIndexes']:
                print(f"  - Index Name: {gsi['IndexName']}")
                print("    Key Schema:")
                for key in gsi['KeySchema']:
                    print(f"      - {key['AttributeName']}: {key['KeyType']}")
                print("    Projection Type:", gsi['Projection']['ProjectionType'])

        # List Local Secondary Indexes (if any)
        if 'LocalSecondaryIndexes' in table_description:
            print("\nLocal Secondary Indexes:")
            for lsi in table_description['LocalSecondaryIndexes']:
                print(f"  - Index Name: {lsi['IndexName']}")
                print("    Key Schema:")
                for key in lsi['KeySchema']:
                    print(f"      - {key['AttributeName']}: {key['KeyType']}")
                print("    Projection Type:", lsi['Projection']['ProjectionType'])

    except Exception as e:
        print(f"Error retrieving table schema: {e}")

# Execute the function
get_table_schema()
