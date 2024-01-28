from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up SQLiteDB
# SQLALCHEMY_DATABASE_URL = "sqlite:///./my-fast-api.db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# Set up Postgresql 
# DATABASE_URI = 'postgresql://postgres:<password>@localhost/<name_of_the_datbase>'
URL_DATABASE = 'postgresql://postgres:030845@localhost:5432/MobileDBSTP'

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
