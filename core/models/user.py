from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer
from typing import List

from core.db_templates import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    user_id: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(nullable=True)
    first_name: Mapped[str] = mapped_column(nullable=True)
    rating: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    
    interactive_history: Mapped[List["InteractiveHistory"]] = relationship("InteractiveHistory", back_populates="user")

