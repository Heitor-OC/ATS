from sqlalchemy import Column, Integer, String
from .database import Base

class PDFContent(Base):
    __tablename__ = "pdf_contents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    content = Column(String)
    search_words = Column(String)

