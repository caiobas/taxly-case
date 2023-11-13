import re
from main.data_extraction.regexPatterns import amount_pattern

def get_amount(pdf_text, data_extracted):

    amount_matches = re.findall(amount_pattern, pdf_text)
    if amount_matches:
        amount = __get_doc_amount(amount_matches)
        data_extracted['amount'] = amount
    
    return data_extracted

def __get_doc_amount(amounts):
    max = 0
    for amount in amounts:
        amount_float = float(amount.replace('.', '').replace(',', '.'))
        if amount_float > max:
            max = amount_float

    return max