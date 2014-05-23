from flask import Flask, request, render_template
#from store import redis
import redis as Redis
from collections import namedtuple

Book = namedtuple("book", ["title", "price", "isbn"], verbose=False)

books = [Book(title='Reflection Groups and Coxeter Groups (Cambridge Studies in Advanced Mathematics)', price='$59.95', isbn='9780521375108'),
Book(title='Instantons and Four-Manifolds (Undergraduate Texts in Mathematics)', price='$18.50', isbn='0387960368'),
Book(title="Thomas' Calculus Early Transcendentals (11th Edition)", price='$160.00', isbn='9780321198006')]

# for book in books:
#     print book.title
redis = Redis.from_url( "redis://redistogo:e53d9c9eee21af1cb977ac1c75e493e2@angelfish.redistogo.com:9536/")
app = Flask(__name__)

@app.route('/')
def hello():
    entries = books
    return render_template("comm.html", entries=entries)


@app.route('/', methods=['POST'])
def communicate_post():
    return request.args.getlist('wanted')
    # if request.form['my-form'] == 'Send':
    #     name = request.form['text']
    #     redis.set('name',name)
    #     return render_template("communicate.html", name=name)
    # elif request.form['my-form'] == 'Refresh':
    #     name = redis.get('name').decode('utf-8')
    #     return render_template("communicate.html", name=name)
    # else:
    #     return "Something went wrong"

if __name__ == "__main__":
    app.run(debug=True)
