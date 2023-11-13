from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config import Config

client = MongoClient(Config.MONGO_URI, server_api=ServerApi('1'))