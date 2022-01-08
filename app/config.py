import os
from starlette.config import Config

dir_path = os.path.dirname(os.path.realpath(__file__))
root_dir = dir_path[:-3]
config = Config(f'{root_dir}.env')

DATABASE_URL = f'sqlite:///' + config('DB_NAME', cast=str)

# Mongo
mongo_config = Config(f'{root_dir}.env.example')

MONGO_USER = mongo_config('MONGO_INITDB_ROOT_USERNAME')
MONGO_PASSWORD = mongo_config('MONGO_INITDB_ROOT_PASSWORD')
MONGO_HOST = mongo_config('MONGO_HOST')
MONGO_PORT = int(mongo_config('MONGO_PORT'))
MONGO_DB = 'mongo'
