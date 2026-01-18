from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

# If you want to use PostgreSQL, uncomment the following lines and comment out the SQLite lines
# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# print("Database URL is ",SQLALCHEMY_DATABASE_URL)
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Using SQLite for simplicity; switch to PostgreSQL by uncommenting above lines
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SESSIONLOCAL = sessionmaker(autocommit=False, autoflush=False,bind=engine)