from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .database import Base
from datetime import datetime


class BlogModel(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    title = Column(String)
    content = Column(String)
    created = Column(DateTime, default=datetime.utcnow)
    is_published = Column(Boolean, default=False)
