import re
from main.data_extraction.regexPatterns import doc_type_patterns

def get_doc_type(pdf_text, data_extracted):

    for doc_type, doc_type_pattern in doc_type_patterns.items():
        doc_type_match = re.search(doc_type_pattern, pdf_text)

        if doc_type_match:
            data_extracted['doc_type'] = doc_type
            return data_extracted

    data_extracted['doc_type'] = 'UNKNOWN'
    return data_extracted