from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

from app import routes