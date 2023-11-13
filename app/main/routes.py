from flask import request, jsonify
from main import bp, docData
from authenticate import authenticate_request
from main.data_extraction.extractData import extract_data
from datetime import datetime as d
from pdfminer.pdfparser import PDFSyntaxError

@bp.route('/upload', methods=['POST'])
def upload():
    authenticate_request()
    if 'files[]' not in request.files:
        return 'No file part'

    files = request.files.getlist('files[]')
    data_extracted = { 'data': [] }

    for file in files:
        obj = {}
        try:
            obj = {
                'filename': file.filename,
                'extrated_data': extract_data(file)
            }
        except PDFSyntaxError as e:
            obj = {
                'filename': file.filename,
                'error': 'File is not a PDF'
            }
    
        except Exception as e:
            obj = {
                'filename': file.filename,
                'error': str(e)
            }
        
        finally:
            data_extracted['data'].append(obj)
    
    __sendDataToDb(data_extracted)

    return jsonify(data_extracted['data'])

def __sendDataToDb(data_extracted):
    data_extracted['request-datetime'] = d.now().isoformat()
    docData.insert_one(data_extracted)