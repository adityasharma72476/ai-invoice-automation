import re

def parse_invoice_data(text: str):
    data = {
        'vendor' : None,
        'date' : None,
        'invoice_number' : None,
        'amount' : None
    }

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if lines:
        data['vendor'] = lines[0]

    
    date_match = re.search(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2},\s+\d{4}", text, re.IGNORECASE)
    if date_match:
        data['date'] = date_match.group()


    invoice_match = re.search(r"Invoice\s*number[:\s]*([A-Z0-9\-]+)", text, re.IGNORECASE)
    if invoice_match:
        data['invoice_number'] = invoice_match.group(1)


    amount_match =  re.search(r"Total\s*\$?([\d,]+\.?\d*)", text, re.IGNORECASE)
    if amount_match:
        data['amount'] = amount_match.group(1)


    return data