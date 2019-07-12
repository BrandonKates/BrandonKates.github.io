import os
from flask import render_template
from flask import Flask

os.environ['FLASK_APP'] = "app"
os.environ['FLASK_ENV'] = "development"

app = Flask(__name__, )#instance_relative_config=True)

# Load the configuration from the instance folder
#app.config.from_pyfile('config.py')


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
	return render_template('index.html')