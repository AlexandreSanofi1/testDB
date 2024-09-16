from pymongo import MongoClient
from datetime import datetime
import time
import os
from dotenv import load_dotenv
import ssl

# Load environment variables from the .env file
load_dotenv()

# Get the MongoDB URI from the .env file
mongodb_uri = os.getenv("MONGODB_URI")

# Path to the downloaded AWS DocumentDB root certificate
ca_file_path = './global-bundle.pem'
if not os.path.exists(ca_file_path):
    print("Certificate file not found.")
    exit()

# Initialize the MongoDB client with SSL settings
client = MongoClient(
    mongodb_uri,
    tls=True,
    tlsCAFile=ca_file_path,
    tlsAllowInvalidHostnames=True  # DocumentDB's certificates may not have the hostname, hence this is needed
)

# Directly get the specified database in the URI
db = client.get_default_database()
collection = db['testCollection']  # Replace with your collection name

# Record the start time
start_time = time.time()

# List to hold the batch of documents
documents = []

# Loop to create 1000 items to insert into the MongoDB collection
for i in range(1, 1001):
    # Construct the document
    document = {
        'TestID': str(i),  # Unique identifier (TestID 1 to 1000)
        'AttributeName': f'SampleAttribute{i}',  # Example of dynamic attribute
        'TimeStamp': str(datetime.now())  # Current timestamp
    }

    # Append the document to the list
    documents.append(document)

    # Insert in batches of 100 items
    if i % 100 == 0:
        collection.insert_many(documents)  # Insert all documents in the batch
        print(f'{i} items written to MongoDB.')
        documents = []  # Clear the list after each batch

# Insert any remaining documents that weren't inserted in the batch (if total count isn't a multiple of 100)
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
print(f"Total time taken to insert 1000 items: {total_time:.2f} seconds")
