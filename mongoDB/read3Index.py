from pymongo import MongoClient
import os
import time
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the MongoDB URI from the .env file
mongodb_uri = os.getenv("MONGODB_URI")

# Initialize the MongoDB client and select the database and collection
client = MongoClient(mongodb_uri)
db = client.get_database()  # Use the default database in the URI
collection = db['testCollection']  # Replace with your collection name

# Query to find documents where all three fields have a value greater than 50
query = {
    '$and': [
        {'RandomNumber1': {'$gt': 50}},
        {'RandomNumber2': {'$gt': 50}},
        {'RandomNumber3': {'$gt': 50}}
    ]
}

# Record the start time
start_time = time.time()

# Execute the query and get the results
results = collection.find(query)

# Count the total number of documents found
total_documents = collection.count_documents(query)

# Record the end time
end_time = time.time()

# Calculate the total time taken
total_time = end_time - start_time

# Convert start and end time to human-readable format
start_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
end_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))

# Print the results
for document in results:
    print(document)

# Print the total number of documents and the time taken
print(f"Total documents found: {total_documents}")
print(f"Start time: {start_time_readable}")
print(f"End time: {end_time_readable}")
print(f"Total time taken for the query: {total_time:.2f} seconds")

"""
Total documents found: 129
Start time: 2024-09-18 20:22:53
End time: 2024-09-18 20:22:54
Total time taken for the query: 0.72 seconds
"""