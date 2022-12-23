from flask import Flask
import random

app = Flask(__name__)

no = random.randint(0, 9)


@app.route('/')
def hello_world():
    return '<h1>Guess the number between 1 to 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:guess>')
def guess_no(guess):
    if guess > no:
        return '<h1>Guess the number between 1 to 9</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">' \
               '<h3>Too Fast</h3>'
    elif guess < no:
        return '<h1>Guess the number between 1 to 9</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">' \
               '<h3>Too Slow</h3>'
    else:
        return '<h1>Guess the number between 1 to 9</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">' \
               '<h3>Perfect😉</h3>'


if __name__ == "__main__":
    app.run(debug=True)
