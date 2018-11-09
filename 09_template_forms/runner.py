from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/signup_form')
def signup_form():
	return render_template('signup_form.html')

@app.route('/thank_you')
def thank_you():
	first = request.args.get('First')
	last = request.args.get('Last')
	return render_template('thank_you.html', first=first, last=last)

if __name__ == '__main__':
	app.run()
