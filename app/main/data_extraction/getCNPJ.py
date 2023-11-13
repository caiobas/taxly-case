import re
from main.data_extraction.regexPatterns import cnpj_pattern
def get_cnpj(pdf_text, data_extracted):

    cnpj_match = re.search(cnpj_pattern, pdf_text)
    if cnpj_match:
        cnpj = cnpj_match.group(0)
        data_extracted['cnpj'] = cnpj
    
    return data_extracted
