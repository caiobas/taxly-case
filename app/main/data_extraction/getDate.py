import re
from main.data_extraction.regexPatterns import date_pattern

def get_date(pdf_text, data_extracted):

    date_match = re.search(date_pattern, pdf_text)
    if date_match:
        date = date_match.group(0)
        
        if data_extracted['receipt']:
            data_extracted['payment_date'] = date
        else:
            data_extracted['due_date'] = date
    
    return data_extracted