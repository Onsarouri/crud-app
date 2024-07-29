from sqlalchemy.ext.asyncio import create_async_engine #creates an asynchronous engine for connecting to the db
from sqlalchemy.orm import DeclarativeBase # as a base class for declarative class definitions
from dotenv import load_dotenv # load variables from .env
import os # for the database connection URLs


load_dotenv()


#engine object to connect to db
engine = create_async_engine(
    url= os.getenv('DATABASE_URL'),
    echo = True
)


#base class for creating database models
class Base(DeclarativeBase):
    pass
#check