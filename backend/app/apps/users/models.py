from sqlalchemy.orm import Mapped, mapped_column

from apps.core.base_models import Base

#user assa
class User(Base):
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True, index=True)
