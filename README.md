# AI Invoice Automation System

## Overview
A FastAPI-based backend system to automate invoice processing using OCR.

## Features
- Upload invoice images or PDFs
- Extract text using Tesseract OCR
- Parse invoice fields:
  - Vendor
  - Date
  - Invoice Number
  - Amount
- Store records in SQLite database
- REST API endpoints

## Tech Stack
- Python
- FastAPI
- Tesseract OCR
- SQLite
- SQLAlchemy

## Run Locally

```bash
pip install -r requirement.txt
uvicorn app.main:app --reload
