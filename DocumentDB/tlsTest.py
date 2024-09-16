from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the MongoDB URI from the .env file
mongodb_uri = os.getenv("MONGODB_URI")

# Path to the downloaded AWS DocumentDB root certificate
ca_file_path = './global-bundle.pem'
if not os.path.exists(ca_file_path):
    print("Certificate file not found.")
    exit()

try:
    # Initialize the MongoDB client with SSL settings
    client = MongoClient(
        mongodb_uri,
        tls=True,
        tlsCAFile=ca_file_path,
        tlsAllowInvalidHostnames=True  # Only use if needed
    )

    # Attempt to connect to the server
    client.admin.command('ping')
    print("Connected successfully to DocumentDB")
except Exception as e:
    print(f"Error connecting to DocumentDB: {e}")
