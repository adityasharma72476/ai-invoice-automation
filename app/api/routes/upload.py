from fastapi import APIRouter, FastAPI, UploadFile, File
import os
import shutil

from app.services.ocr_services import extract_text_from_image
from app.services.parser_service import parse_invoice_data

from app.database import SessionLocal
from app.models.invoice import Invoice

router = APIRouter(tags=['Upload'])

UPLOAD_DIR = 'app/uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post('/upload')
def upload_invoice(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_image(file_path)

    parsed_data = parse_invoice_data(extracted_text)

    db = SessionLocal()

    new_invoice = Invoice(
        vendor = parsed_data['vendor'],
        date = parsed_data['date'],
        invoice_number = parsed_data['invoice_number'],
        amount = parsed_data['amount'],
        filename = file.filename
    )

    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)
    db.close()

    return {
        'filename': file.filename,
        'message': 'File Uploaded Successfully',
        'raw_text': extracted_text,
        'structured_data': parsed_data
    }