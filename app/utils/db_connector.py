import pandas as pd
from pymongo import MongoClient
from app import config


class MongoConnector:
    def __init__(self):
        self.client = MongoClient(
            username=config.MONGO_USER,
            password=config.MONGO_PASSWORD,
            host=config.MONGO_HOST,
            port=config.MONGO_PORT,
            connect=True,
            maxPoolSize=2
        )
        self.db = self.client[config.MONGO_DB]

    # Load
    def load_model(self, unit_id, subsystem_id):
        model = self.db.models_info.find_one({"unit_id": unit_id,
                                                     "subsystem_id": subsystem_id})
        return model

    def update_model(self, unit_id, subsystem_id, new_config, key=None, sub_key=None):
        self.db.models_info.update_one({"unit_id": unit_id,
                                        "subsystem_id": subsystem_id},
                                       {'$set': new_config}, upsert=True)
