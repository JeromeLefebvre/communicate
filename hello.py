from flask import Flask, request, render_template
from redis_to_tuple import allBooks
from flask.ext.mail import Mail, Message
from store import redis

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

@app.route('/')
def intial():
    books = allBooks()
    return render_template("comm.html", entries=sorted(books, key=lambda entry: entry.author))

@app.route('/', methods=['POST'])
def communicate_post():
    requested_books = request.form.getlist('wanted')
    if len(requested_books) == 0:
        entries = books
        return render_template("comm.html", entries=books)
    else:
        list_of_books = ''
        for isbn in requested_books:
            list_of_books += redis.get(isbn).decode('utf-8') + "\n"
        name = request.form['name']
        email = request.form['email']
        msg =  Message("Hello here are the requested books", sender="jeorme.8675309@gmail.com",  recipients=["jerome.p.lefebvre@gmail.com"])
        msg.body = name + " who can be contacted at " + email + " wants:\n"
        
        msg.body += list_of_books
        mail.send(msg)

        name = request.form['name']
        email = request.form['email']
        msg =  Message("Hello here are the books you requested", sender="jerome.p.lefebvre@gmail.com",  recipients=[email])
        #msg.body = name + " who can be contacted at " + email + " wants:\n"
        msg.body = ''
        for isbn in requested_books:
            msg.body += redis.get(isbn).decode('utf-8').split(':::')[0] + "\n"
        mail.send(msg)        
    return 'Thank you! An email is being sent to you about the books.'

if __name__ == "__main__":
    app.run(debug=True)

