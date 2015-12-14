from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
	
	posts = [
	    {
		'author' : {'nickname': 'John'},
		'body' : 'Movie on Sunday?'
	    },
	    {
		'author' : {'nickname': 'Obama'},
		'body' : 'You are the next U.S. President'
	    }
	]
	return render_template('hello.html', name=name, posts = posts)

if __name__ == '__main__':
	app.run()
