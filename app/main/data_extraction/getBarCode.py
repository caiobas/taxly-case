import re
from main.data_extraction.regexPatterns import bar_code_pattern

def get_bar_code(pdf_text, data_extracted):

    bar_code_match = re.search(bar_code_pattern, pdf_text)
    if bar_code_match:
        bar_code = bar_code_match.group(0)
        data_extracted['bar_code'] = bar_code
    
    return data_extracted