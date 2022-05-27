from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

user = "trainer"
password = "trainer1"
url = "localhost:5432"
database = "fitnes"

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{url}/{database}".format(user=user, password=password,
                                                                                    url=url, database=database)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=3, max_overflow=0
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ToDo Реализовать занесение данных при запуске

# with engine.connect() as con:
#     with open("initialData") as file:
#         print("hello    1")
#         for line in file:
#             print("hello    2" + line.rstrip())
#             # query = text(line.rstrip())
#             # con.execute(query)

