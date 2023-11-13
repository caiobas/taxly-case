from flask import Blueprint
from extensions import client

bp = Blueprint('main', __name__)

db = client.documents
docData = db.docData

from main import routes