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

mongo = MongoConnector()

simple_model = {'user_id': 'first_user',
                'email': 'qsqw@edwe.ewdwe',
                'nickname': 'qwerty'}
mongo.update_model(user_id='first_user', new_config=simple_model)

check_mongo()

update_model = mongo.load_model(user_id='first_user')
print(update_model)
