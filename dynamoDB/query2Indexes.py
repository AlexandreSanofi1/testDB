import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

# Reference the table name
table_name = 'test30Indexes'

def multi_index_query():
    print("Attempting to query using multiple indexes...")
    try:
      
        response = dynamodb.query(
            TableName=table_name,
           
            IndexName='index1,index2',  
            KeyConditionExpression='TestID = :test_id',
            ExpressionAttributeValues={
                ':test_id': {'S': '1'}
            }
        )
        print("Items found:", len(response.get('Items', [])))
    except Exception as e:
        print(f"Error during multi-index query attempt: {e}")


multi_index_query()

"""
(venv) alleonet@Alexandres-MBP dynamoDB % python3 query2Indexes.py 
Attempting to query using multiple indexes...
Error during multi-index query attempt: An error occurred (ValidationException) when calling the Query operation: 1 validation error detected: Value 'index1,index2' at 'indexName' failed to satisfy constraint: Member must satisfy regular expression pattern: [a-zA-Z0-9_.-]+
(venv) alleonet@Alexandres-MBP dynamoDB % 

"""