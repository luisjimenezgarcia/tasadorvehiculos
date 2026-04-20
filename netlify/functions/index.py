from flask import Flask
from serverless_wsgi import handle_request

import sys
import os

# Añadir la raíz del proyecto al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Importar tu aplicación original
from app import app as application

def handler(event, context):
    return handle_request(application, event, context)
