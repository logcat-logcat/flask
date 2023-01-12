from flask import Flask
from flask import render_template
from flask import request
from flask import make_response


app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index_page():
	c_id = request.cookies.get('id')
	c_pas = request.cookies.get('pass')
	return render_template('voca_cookie.html', id = c_id, pas = c_pas)
	
@app.route('/login', methods = ['POST'])
def login():
	
	id = request.form['id']
	pas = request.form['pass']
	resp = make_response("id : "+id+" pass : "+pas)
	resp.set_cookie('id', id)
	resp.set_cookie('pass', pas)
	return resp

if __name__ == '__main__':
    app.run(host='210.114.22.121', port = 5500)