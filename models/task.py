from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from db.session import Base


class TaskORM(Base):

    __tablename__ = "tasks"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)