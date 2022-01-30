import os
from starlette.config import Config
from starlette.datastructures import Secret

dir_path = os.path.dirname(os.path.realpath(__file__))
root_dir = dir_path[:-3]
config = Config(f'{root_dir}.env')

DATABASE_URL = f'sqlite:///' + config('DB_NAME', cast=str)

SECRET_KEY = config("SECRET_KEY", cast=Secret)

# POSTGRES
PG_USER = config("POSTGRES_USER", cast=str)
PG_PASSWORD = config("POSTGRES_PASSWORD", cast=str)
PG_HOST = config("POSTGRES_HOST", cast=str)
PG_PORT = config("POSTGRES_PORT", cast=int)
PG_DB = config("POSTGRES_DB", cast=str)
PG_URL = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
