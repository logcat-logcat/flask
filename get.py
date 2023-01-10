from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')

def index_page():
    return "Hellow world!"

	


@app.route('/test', methods = ['GET'])
def login():
	
	temp = request.args.get('id', '')
	temp2 = request.args.get('pass', '')
	
	return "id : "temp + ", " + "pass : " +temp2

if __name__ == '__main__':
    app.run(host='210.114.22.121', port = 5550)