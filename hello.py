from flask import Flask, request, render_template
from redis_to_tuple import allBooks

app = Flask(__name__)

books = allBooks()

@app.route('/', methods=['GET'])
def communicate_post():
    a = request.args.getlist('wanted')
    if len(a) == 0:
        entries = books
        return render_template("comm.html", entries=entries)
    else:
        # Now need email here
        return str(a)

if __name__ == "__main__":
    app.run(debug=True)
