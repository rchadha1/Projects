from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "Index Page"

@app.route('/hello')
def hello():
	return "Hello World"

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username

@app.route('/projects/')
def projects():
    return 'The project page'

if __name__ == "__main__":
	
	app.run()
