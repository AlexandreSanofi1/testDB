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

# Loop to insert 1000 items into the MongoDB collection
for i in range(1, 1001):
    # Construct the document
    document = {
        'TestID': str(i),  # Unique identifier (TestID 1 to 1000)
        'AttributeName': f'SampleAttribute{i}',  # Example of dynamic attribute
        'TimeStamp': str(datetime.now())  # Current timestamp
    }

    # Insert the document into the collection
    collection.insert_one(document)

    # Print progress every 100 items
    if i % 100 == 0:
        print(f'{i} items written to MongoDB.')

    # Optional: Add a small delay to avoid overwhelming the database
    time.sleep(0.01)  # 10ms delay to prevent overwhelming the collection

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
