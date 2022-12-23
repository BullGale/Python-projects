from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
           '<h3>BYE bYE</h3>'

@app.route("/bye")
def say_bye():
    return "Bye"

@app.route("/<name>")
def greet(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True)
