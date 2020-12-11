from flask import Flask
from flask_project.app.config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)