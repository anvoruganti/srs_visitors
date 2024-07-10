import datetime
from pymongo import MongoClient # type: ignore
from backend.config import Config

client = MongoClient(Config.MONGO_URI)
db = client[Config.DB_NAME]
visitor_collection = db[Config.COLLECTION_NAME]

class VisitorModel:
    @staticmethod
    def get_visitor(new_id):
        return visitor_collection.find_one({"NewId": new_id})
    
    @staticmethod
    def check_in_visitor(new_id):
        return visitor_collection.update_one(
            {"NewId": new_id},
            {"$set": {"IsCheckedIn": True, "CheckInTime": datetime.datetime.utcnow()}}
        )