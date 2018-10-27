from flask import render_template, request
from app import app
from schedule_api import get_terms

@app.route('/')
def index():
    options = {}
    try:
        options['terms'] = get_terms()
    except:
        options['api_error'] = True

    return render_template('index.html', **options)

@app.route('/projects/')
def projects():
	return render_template('projects.html')
	
@app.route('/base-japanese')
def base-japanese():
	return render_template('base-japanese.html');