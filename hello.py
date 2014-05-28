from flask import Flask, request, render_template
from redis_to_tuple import allBooks
from flask.ext.mail import Mail, Message
from store import redis

app = Flask(__name__)

books = allBooks()
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

@app.route('/')
def intial():
    return render_template("comm.html", entries=books)

@app.route('/', methods=['GET'])
def communicate_post():
    requested_books = request.args.getlist('wanted') 
    if len(requested_books) == 0:
        entries = books
        return render_template("comm.html", entries=entries)
    else:
        name = request.args['name']
        email = request.args['email']
        msg =  Message("Hello here are the requested books", sender="jeorme.8675309@gmail.com",  recipients=["jerome.p.lefebvre@gmail.com"])
        msg.body = name + " who can be contacted at " + email + " wants:\n"
        for isbn in requested_books:
            msg.body += redis.get(isbn).decode('utf-8') + "\n" 

        mail.send(msg)
    return 'Thank you!'

if __name__ == "__main__":
    app.run()

