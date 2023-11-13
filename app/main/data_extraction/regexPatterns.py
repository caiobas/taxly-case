from main.enum.docTypeEnum import DocType

amount_pattern = r'\b\d{1,3}(?:\.\d{3})*(?:,\d+)\b'
receipt_pattern = r'Comprovante'
cnpj_pattern = r'(?:\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2})'
bar_code_pattern = r'(\d{11}-?\d?) (\d{11}-?\d?) (\d{11}-?\d?) (\d{11}-?\d?)'
social_reason_pattern = r'\b(?:[A-Z]+\s)+?(ME|EPP|EIRELI|LTDA|S\.A\.)\b'
date_pattern = r'\b(?:0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b'
doc_month_pattern = r'\s(0?[1-9]|1[0-2])/(19|20)\d{2}|(Janeiro|Fevereiro|Março|Abril|Maio|Junho|Julho|Agosto|Setembro|Outubro|Novembro|Dezembro)/(19|20)\d{2}'

doc_type_patterns = {
    DocType.DAS: r'Documento de Arrecadação do Simples Nacional', 
    DocType.DAMSP: r'DAMSP - Documento de Arrecadação do Município de São Paulo'
}