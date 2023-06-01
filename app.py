from flask import Flask


app = Flask(__name__)
@app.route('/')

"""
Doc
"""
def index():
    return '<h1>Hello WSB! Greetings from Flask!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
