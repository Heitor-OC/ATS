# schemas.py
from pydantic import BaseModel
from typing import Optional

class PDFContentBase(BaseModel):
    filename: str
    content: str
    search_words: Optional[str] = None 

class PDFContentCreate(PDFContentBase):
    pass

class PDFContent(PDFContentBase):
    id: str  

    class Config:
        orm_mode = True
