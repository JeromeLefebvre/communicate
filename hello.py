from flask import Flask, request, render_template
#from store import redis
import redis as Redis

redis = Redis.from_url( "redis://redistogo:e53d9c9eee21af1cb977ac1c75e493e2@angelfish.redistogo.com:9536/")
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
