from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from .schemas import PDFContentCreate

async def create_pdf_content(db: AsyncIOMotorDatabase, pdf_content: PDFContentCreate):
    document = pdf_content.dict()
    result = await db.pdf_contents.insert_one(document)
    document['id'] = str(result.inserted_id)
    return document

async def get_pdf_content(db: AsyncIOMotorDatabase, pdf_content_id: str):
    return await db.pdf_contents.find_one({"_id": ObjectId(pdf_content_id)})

async def get_pdf_contents(db: AsyncIOMotorDatabase, skip: int = 0, limit: int = 10):
    pdfs = await db.pdf_contents.find().skip(skip).limit(limit).to_list(length=limit)
    for pdf in pdfs:
        pdf["id"] = str(pdf["_id"])
    return pdfs

async def delete_pdf_content(db: AsyncIOMotorDatabase, pdf_content_id: str):
    result = await db.pdf_contents.delete_one({"_id": ObjectId(pdf_content_id)})
    return result.deleted_count > 0

async def delete_search_words(db: AsyncIOMotorDatabase, pdf_content_id: str):
    result = await db.pdf_contents.update_one({"_id": ObjectId(pdf_content_id)}, {"$unset": {"search_words": ""}})
    return result.matched_count > 0
