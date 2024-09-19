from pymongo import MongoClient
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

# Query to find the first 1000 documents
cursor = collection.find().limit(1000)

# Read and print the documents
documents = list(cursor)  # Convert cursor to a list to read documents
print(documents)

# Count the number of documents read
total_items_read = len(documents)

# Record the end time
end_time = time.time()

# Calculate the total time taken
total_time = end_time - start_time

# Convert start and end time to human-readable format
start_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
end_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))

# Print the total items read, start time, end time, and total time
print(f"Total items read: {total_items_read}")
print(f"Start time: {start_time_readable}")
print(f"End time: {end_time_readable}")
print(f"Total time taken to read 1,000 items: {total_time:.2f} seconds")

# Optionally, print the documents (can be large output)
# print(documents)
