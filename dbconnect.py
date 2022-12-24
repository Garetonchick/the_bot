from sqlalchemy import create_engine
from os import getenv

engine = create_engine(
    "postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}".format(
        db_username=getenv('DB_USERNAME'), 
        db_password=getenv('DB_PASSWORD'),
        db_host=getenv('DB_HOST'),
        db_port=getenv('DB_PORT'),
        db_name=getenv('DB_NAME')
    ),
    echo=True
)

def create_connection():
    return engine.connect()