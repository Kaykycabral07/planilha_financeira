from sqlalchemy import String, Integer, DateTime, ForeignKey, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime



class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    data_creation: Mapped[datetime] = mapped_column(DateTime)
    password: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, nome={self.name}, email={self.email}, data_de_criacao={self.data_creation} )>"


class Transaction(Base):
    __tablename__ = "movimentacao_financeira"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("usuario.id") )
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    value: Mapped[float] = mapped_column(Float, nullable=False)