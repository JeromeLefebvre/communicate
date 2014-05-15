
from flask import Flask, render_template
from store import redis

app = Flask(__name__)


@app.route('/')
def hello():
    #name = redis.get('name').decode('utf-8')
    name = "Chris"
    return render_template("communicate.html", name=name)


@app.route('/', methods=['POST'])
def my_form_post():
    print("Called")
    if request.form['my-form'] == 'Send':
        return render_template("communicate.html", name='send')
    elif request.form['my-form'] == 'Refresh':
        return render_template("communicate.html", name='refresh')

if __name__ == "__main__":
	app.run()
