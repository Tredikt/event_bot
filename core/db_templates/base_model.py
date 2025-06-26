from datetime import datetime
from sqlalchemy import DateTime, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class BaseModel(DeclarativeBase):
    is_active: Mapped[bool] = mapped_column(default=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        server_default=text("CURRENT_TIMESTAMP")  # SQLite поддерживает только UTC
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=datetime.utcnow  # обновление через Python
    )