import re
from main.data_extraction.regexPatterns import doc_month_pattern

def get_doc_month(pdf_text, data_extracted):
    doc_month_match = re.search(doc_month_pattern, pdf_text)

    if doc_month_match:
        doc_month = doc_month_match.group(0)
        data_extracted['doc_month'] = doc_month.strip()
    
    return data_extracted