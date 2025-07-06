from sqlalchemy.orm import Mapped, mapped_column

from core.db_templates import BaseModel


class Speaker(BaseModel):
    __tablename__ = 'speaker'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=True, default=None)