import re
from main.data_extraction.regexPatterns import social_reason_pattern

def get_social_reason(pdf_text, data_extracted):
    social_reason_match = re.search(social_reason_pattern, pdf_text)

    if social_reason_match:
        social_reason = social_reason_match.group(0)
        data_extracted['social_reason'] = social_reason
    
    return data_extracted