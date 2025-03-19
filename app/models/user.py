from datetime import datetime
from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"<User {self.name}>"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
