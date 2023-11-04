from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

compose_db_url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="postgres",
    host="db",
    database="wikiprof",
    port="5432",
)

local_db_url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="postgres",
    host="localhost",
    database="wikiprof",
    port="5432",
)

engine = create_engine(compose_db_url)
# engine = create_engine(local_db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
