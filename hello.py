
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')

def index_page():
    return "Hellow world!"

@app.route('/main')

def main_page():
    return "This is main page!!"
	



if __name__ == '__main__':
    app.run(host='210.114.22.121', port = 5550)
