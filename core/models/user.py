from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, DateTime
from typing import List

from core.db_templates import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    user_id: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(nullable=True)
    first_name: Mapped[str] = mapped_column(nullable=True)
    rating: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    feedback_waiting: Mapped[datetime] = mapped_column(default=None, nullable=True)

    interactive_history: Mapped[List["InteractiveHistory"]] = relationship(argument="InteractiveHistory", back_populates="user")
    feedback: Mapped["Inside"] = relationship(argument="Feedback", back_populates="user")
    question: Mapped["Question"] = relationship(argument="Question", back_populates="user")