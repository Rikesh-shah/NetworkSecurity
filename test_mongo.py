from pymongo.mongo_client import MongoClient
from networksecurity.logging import logger
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

uri = MONGO_DB_URL

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    logger.logging.info("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    logger.logging.error(e)