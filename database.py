from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = "trainer"
password = "trainer1"
url = "db:5432"
database = "fitnes"

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{url}/{database}".format(user=user, password=password,
                                                                                    url=url, database=database)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=3, max_overflow=0
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
