from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/')

def index_page():
    return render_template('flask_form.html')

@app.route('/login', methods = ['POST'])
def login():
	
	id = request.form['id']
	pas = request.form['pass']
	
	return "id : " + id + ", " + "pass : " + pas

if __name__ == '__main__':
    app.run(host='210.114.22.121', port = 5550)