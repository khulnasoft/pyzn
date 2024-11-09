import logging
import os

MONGODB = "mongodb://mongodb:27017"

WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ.get("PYZN_SECRET_KEY")

ADMIN_PASSWORD = os.environ.get("PYZN_ADMIN_PASSWORD")
BQ_CREDENTIALS_FILE = os.environ.get("PYZN_BIGQUERY_CREDENTIALS")
LOGGING_DIR = "logs"
LOGGING_FILE = os.environ.get("PYZN_LOGGING_FILE")
LOGGING_LEVEL = logging.DEBUG
