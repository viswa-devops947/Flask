from flask import Flask,render_template

app = Flask(__name__)

@app.route('/<user_name>')
def index(user_name):
	return render_template('index.html', user_name=user_name)

if __name__ == '__main__':
	app.run(debug=True)