from app.utils.db_connector import MongoConnector
from app import config

print(config.MONGO_USER)
print(config.MONGO_PASSWORD)
print(config.MONGO_HOST)
print(config.MONGO_PORT)
print(config.MONGO_DB)


def check_mongo():
    mongo = MongoConnector()
    db_and_collection = dict((db, [collection for collection in mongo.client[db].collection_names()])
                             for db in mongo.client.database_names())

    print(db_and_collection)

check_mongo()
