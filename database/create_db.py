from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "postgresql://kayky:fenix1223@localhost:5432/projeto_db"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

Base.metadata.create_all(engine)