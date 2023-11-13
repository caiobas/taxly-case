import pdfplumber
from main.data_extraction.isReceipt import is_receipt
from main.data_extraction.getSocialReason import get_social_reason
from main.data_extraction.getDate import get_date
from main.data_extraction.getBarCode import get_bar_code
from main.data_extraction.getAmount import get_amount
from main.data_extraction.getCNPJ import get_cnpj
from main.data_extraction.getDocMonth import get_doc_month
from main.data_extraction.getDocType import get_doc_type

def extract_data(file):
    pdf_texts = __extract_text_from_pdf(file)
    data_extracted = {}

    for pdf_text in pdf_texts:
        data_extracted = is_receipt(pdf_text, data_extracted)
        data_extracted = get_social_reason(pdf_text, data_extracted)
        data_extracted = get_date(pdf_text, data_extracted)
        data_extracted = get_bar_code(pdf_text, data_extracted)
        data_extracted = get_amount(pdf_text, data_extracted)
        data_extracted = get_cnpj(pdf_text, data_extracted)
        data_extracted = get_doc_month(pdf_text, data_extracted)
        if not data_extracted['receipt']:
            data_extracted = get_doc_type(pdf_text, data_extracted)

    return data_extracted
    
    

def __extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        page_texts = [page.extract_text() for page in pdf.pages]

    return page_texts