from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	users = ['john', 'kennedy', 'patrick']
	return render_template('index.html', users=users)

if __name__ == '__main__':
	app.run(debug=True)