import re
from main.data_extraction.regexPatterns import receipt_pattern

def is_receipt(pdf_text, data_extracted):
    receipt_match = re.search(receipt_pattern, pdf_text)
    data_extracted['receipt'] = False

    if receipt_match:
        data_extracted['receipt'] = True
    
    return data_extracted