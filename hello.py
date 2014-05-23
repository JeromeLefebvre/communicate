from flask import Flask, request, render_template
from store import redis

app = Flask(__name__)

@app.route('/')
def hello():
    name = redis.get('name').decode('utf-8')
    return render_template("communicate.html", name=name)


@app.route('/', methods=['POST'])
def communicate_post():
    if request.form['my-form'] == 'Send':
        name = request.form['text']
        redis.set('name',name)
        return render_template("communicate.html", name=name)
    elif request.form['my-form'] == 'Refresh':
        name = redis.get('name').decode('utf-8')
        return render_template("communicate.html", name=name)
    else:
        return "Something went wrong"

if __name__ == "__main__":
    app.run(debug=True)