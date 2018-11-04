from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello World!</h1>'

@app.route('/information')
def page_info():
	return '<h1>This page gives your information</h2>'

if __name__ == '__main__':
	app.run()