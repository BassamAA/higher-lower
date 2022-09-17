# higher lower game : input in the url your guess of the random number between 0 and 9, it will show you if your answer is correct or not


import random

from flask import Flask
from random import Random

app = Flask(__name__)

n = random.randint(0,9)



@app.route("/")
def hello_world():
    return '<h1> Guess a number between 0 and 9</h1>\n'\
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route("/<int:i>")
def game(i):
    if i < n:
        return '<h1>No it is higher! Try again</h1>\n' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

    elif i > n:
        return '<h1>No it is lower ! Try again</h1>\n' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif i == n:
        return '<h1>Correct answer !</h1>\n' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'



if __name__ == "__main__":
    app.run(debug=True)
