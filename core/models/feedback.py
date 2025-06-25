from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, String
from typing import List

from core.db_templates import BaseModel


class Feedback(BaseModel):
    __tablename__ = "feedback"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("user.user_id"))
    interactive_name: Mapped[str] = mapped_column(String(100), nullable=False)
    rate: Mapped[str]
    inside: Mapped[str] = mapped_column(nullable=True)

    user: Mapped["User"] = relationship(argument="User", back_populates="feedback")

