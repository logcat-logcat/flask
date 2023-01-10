from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')

def index_page():
    return "Hellow world!"

@app.route('/user/<username>')

def show_username(username):
    return "user name = %s" % username
	# 파이썬 문법입니다. 그냥 넘어갈게요

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run(host='210.114.22.121', port = 5550)