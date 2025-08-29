from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, User
from datetime import datetime

DATABASE_URL = "postgresql://kayky:fenix1223@localhost:5432/projeto_db"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

Base.metadata.create_all(engine)

def register_user_in_db(name:str, email:str, password:str):
    new_user = User(name=name, email=email, password=password, data_creation= datetime.now())
    session.add(new_user)
    session.commit()
    
