from sqlalchemy.orm import Mapped, mapped_column

from core.db_templates import BaseModel


class Messages(BaseModel):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    chat_id: Mapped[str]
    message_id: Mapped[int]