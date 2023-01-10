from flask import Flask, url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def index_page():
	return "wow"
    

@app.route('/user/<username>')
def show_username(username):
    return "user name = %s" % username

@app.route('/test/url')
def testurl():
	return url_for('index_page') + url_for('index_page', kk = '쉼표 뒤에것은 그냥 뒤에 붙음') + url_for( 'show_username', username = 'logcat')
	 
	


	
	

if __name__ == '__main__':
    app.run(host='210.114.22.121', port = 5550)