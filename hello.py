from flask import Flask, request, render_template
from redis_to_tuple import allBooks

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

@app.route('/', methods=['GET','POST'])
def communicate_post():
    a = request.args.getlist('wanted') 
    if len(a) == 0:
        entries = books
        return render_template("comm.html", entries=entries)
    else:
        #if request.form['my-form'] == 'Send':
        email = request.form['text']
        msg =  Message("Hello", sender="jeorme.8675309@gmail.com",  recipients=["jeorme.8675309@gmail.com"])
        msg.body = 'I am a roboot tester.'
        msg.body += email
        mail.send(msg)
        return 'Thank you!'

if __name__ == "__main__":
    app.run(debug=True)
