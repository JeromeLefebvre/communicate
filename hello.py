
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "<big><b>hello world!</b></big>"

if __name__ == "__main__":
	app.run()