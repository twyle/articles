#project-name/__init__.py
from flask import Flask
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

from API import routes