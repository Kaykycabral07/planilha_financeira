from sqlalchemy import String, Integer, create_engine, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime



class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    number: Mapped[int] = mapped_column(Integer, nullable=False)
    data_creation: Mapped[datetime] = mapped_column(DateTime)
    password: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, nome={self.name}, email={self.email}, telefone={self.number}, data_de_criacao={self.data_creation} )>"


