from flask import render_template
from app import app


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
@app.route('/main', methods=['POST', 'GET'])
def home():
    return render_template('home.html', title='Welcome')
