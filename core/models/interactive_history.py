from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey
from datetime import datetime

from core.db_templates import BaseModel


class InteractiveHistory(BaseModel):
    __tablename__ = "interactive_history"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    interactive_name: Mapped[str] = mapped_column(String(100), nullable=False)
    points_earned: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    completed_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    
    user: Mapped["User"] = relationship("User", back_populates="interactive_history") 