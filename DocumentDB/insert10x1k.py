from pymongo import MongoClient
from datetime import datetime
import time
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the MongoDB URI from the .env file
mongodb_uri = os.getenv("MONGODB_URI")

# Initialize the MongoDB client and select the database and collection
client = MongoClient(mongodb_uri)
db = client.get_database()  # Use the default database in the URI
collection = db['testCollection']  # Replace with your collection name

# Record the start time
start_time = time.time()

# List to hold the batch of documents
documents = []

# Loop to create 10,000 items to insert into the MongoDB collection
for i in range(1, 10001):
    # Construct the document
    document = {
        'TestID': str(i),  # Unique identifier (TestID 1 to 10000)
        'AttributeName': f'SampleAttribute{i}',  # Example of dynamic attribute
        'TimeStamp': str(datetime.now())  # Current timestamp
    }

    # Append the document to the list
    documents.append(document)

    # Insert in batches of 1000 items
    if i % 1000 == 0:
        collection.insert_many(documents)  # Insert all documents in the batch
        print(f'{i} items written to MongoDB.')
        documents = []  # Clear the list after each batch

# Insert any remaining documents that weren't inserted in the batch
if documents:
    collection.insert_many(documents)
    print(f'{len(documents)} remaining items written to MongoDB.')

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
print(f"Total time taken to insert 10,000 items: {total_time:.2f} seconds")


"""
(myenv) alleonet@Alexandres-MBP mongoDB % python3 insert10x1k.py 
1000 items written to MongoDB.
2000 items written to MongoDB.
3000 items written to MongoDB.
4000 items written to MongoDB.
5000 items written to MongoDB.
6000 items written to MongoDB.
7000 items written to MongoDB.
8000 items written to MongoDB.
9000 items written to MongoDB.
10000 items written to MongoDB.
Start time: 2024-09-13 15:16:33
End time: 2024-09-13 15:16:50
Total time taken to insert 10,000 items: 17.46 seconds
"""
