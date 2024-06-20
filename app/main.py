from fastapi import FastAPI, File, UploadFile, Form, Depends, HTTPException, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import fitz 
from typing import List

from .database import db, ping
from .schemas import PDFContent, PDFContentCreate
from .crud import create_pdf_content, get_pdf_content, get_pdf_contents, delete_pdf_content, delete_search_words

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.on_event("startup")
async def startup_db_client():
    await ping() 

@app.on_event("shutdown")
async def shutdown_db_client():
    db.client.close()



@app.get("/", response_class=HTMLResponse)
def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/uploadpdf/", response_model=PDFContent)
async def upload_pdf(
    file: UploadFile = File(...),
    search_words: str = Form(None),  
):
    contents = await file.read()
    pdf_document = fitz.open(stream=contents, filetype="pdf")
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()

    pdf_content = PDFContentCreate(
        filename=file.filename,
        content=text,
        search_words=search_words 
    )
    
    document = await create_pdf_content(db, pdf_content)
    return document


@app.get("/pdfcontent", response_model=List[PDFContent])
async def get_all_pdfs():
    pdfs = await get_pdf_contents(db)
    return pdfs


@app.delete("/pdfcontent/{pdf_content_id}")
async def delete_pdf_or_search_words(
    pdf_content_id: str,
    delete_search_words: bool = Query(default=False, description="Delete search_words instead of PDF"),
):
    if delete_search_words:
        deleted = await delete_search_words(db, pdf_content_id)
    else:
        deleted = await delete_pdf_content(db, pdf_content_id)

    if not deleted:
        raise HTTPException(status_code=404, detail=f"PDF com ID {pdf_content_id} não encontrado")


@app.get("/pdfcontent/{pdf_content_id}/display")
async def display_pdf_content(pdf_content_id: str, request: Request):
    db_pdf_content = await get_pdf_content(db, pdf_content_id)
    if db_pdf_content is None:
        raise HTTPException(status_code=404, detail="PDF content not found")
    return templates.TemplateResponse("pdf_content.html", {
        "request": request,
        "filename": db_pdf_content["filename"],
        "content": db_pdf_content["content"]
    })


@app.get("/pdfcontent/{pdf_content_id}/search", response_model=dict)
async def search_words_in_pdf(pdf_content_id: str):
    db_pdf_content = await get_pdf_content(db, pdf_content_id)
    if db_pdf_content is None:
        raise HTTPException(status_code=404, detail="PDF content not found")

    search_words = db_pdf_content.get("search_words")
    if not search_words:
        return {"found": [], "not_found": []}

    search_words_list = search_words.split(',')
    content = db_pdf_content["content"]
    words_found = []
    words_not_found = []

    for word in search_words_list:
        word = word.strip()
        if word in content:
            words_found.append(word)
        else:
            words_not_found.append(word)

    return {"found": words_found, "not_found": words_not_found}



@app.get("/pdfcontent/{pdf_content_id}/search/results", response_class=HTMLResponse)
async def search_results_page(pdf_content_id: str, request: Request):
    return templates.TemplateResponse("search_results.html", {
        "request": request,
        "pdf_content_id": pdf_content_id
    })