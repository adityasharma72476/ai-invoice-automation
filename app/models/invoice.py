from sqlalchemy import Column, Integer, String
from app.database import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    vendor = Column(String)
    date = Column(String)
    invoice_number = Column(String)
    amount = Column(String)
    filename = Column(String)