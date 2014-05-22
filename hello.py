
from flask import Flask, request, render_template
from store import redis
from flask.ext.mail import Mail,Message



app = Flask(__name__)
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'jeorme.8675309@gmail.com',
    MAIL_PASSWORD = 'UBCmathematics',
))


mail = Mail(app)

@app.route("/")
def index():

    name = redis.get('name').decode('utf-8')
    return render_template("communicate.html", name=name)

'''
@app.route('/')
def hello():
    name = redis.get('name').decode('utf-8')
    return render_template("communicate.html", name=name)
'''

@app.route('/', methods=['POST'])
def communicate_post():
    if request.form['my-form'] == 'Send':
        msg = Message("Hello", sender="jeorme.8675309@gmail.com",  recipients=["jeorme.8675309@gmail.com"])
        msg.body = "testing send 1 "
        name = request.form['text']
        msg.body += name
        mail.send(msg)
        redis.set('name',name)
        return render_template("communicate.html", name=name)
    elif request.form['my-form'] == 'Refresh':
        name = redis.get('name').decode('utf-8')
        return render_template("communicate.html", name=name)
    else:
        return "Something went wrong"

if __name__ == "__main__":
	app.run(debug=True)
