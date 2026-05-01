from fastapi import FastAPI
from app.api.routes.upload import router as upload_router

from app.database import engine
from app.models.invoice import Invoice


#CREATE TABLE--

Invoice.metadata.create_all(bind = engine)


app =FastAPI(
    title = 'AI Finance automation API',
    description = 'Invoice OCR + Expense Automation Backend',
    version = '1.0.0'
)

@app.get('/')
def home():
    return {'message': 'AI finance automation API is running'}

app.include_router(upload_router, prefix = '/api')

