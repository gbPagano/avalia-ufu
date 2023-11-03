from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

db_url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="postgres",
    host="db",
    database="wikiprof",
    port="5432",
)

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
