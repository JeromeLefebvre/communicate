
from flask import Flask, render_template
from store import redis

app = Flask(__name__)


@app.route('/')
def hello():
    #name = redis.get('name').decode('utf-8')
    name = "Chris"
    return render_template("communicate.html", name=name)


@app.route('/', methods=['POST'])
def communicate_post():
    if request.form['my-form'] == 'Send':
        print("Send")
        name = "Chris"
        return render_template("communicate.html", name=name)
    elif request.form['my-form'] == 'Refresh':
        print("Refresh")
        return render_template("communicate.html", name='refresh')
    else:
        return "Something went wrong"

if __name__ == "__main__":
	app.run()
