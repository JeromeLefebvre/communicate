
from flask import Flask
from store import redis

app = Flask(__name__)

@app.route('/')
def hello():
	name = redis.get('name')
	return "<big><b>hello %s</b></big>" % name

if __name__ == "__main__":
	app.run()
