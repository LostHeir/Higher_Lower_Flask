from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media0.giphy.com/media/IsfrRWvbUdRny/giphy.gif?cid=ecf05e4762x28wepg9rm9iyr8djtcmk09" \
           "rr5edobq0l0rnjp&rid=giphy.gif&ct=g'>"


@app.route("/<int:guess>")
def temp(guess):
    rand_number = random.randint(0, 9)
    if guess > rand_number:
        return "<p style='color:red;font-size:50px'>Too high!</p>" \
               "<img src='https://media0.giphy.com/media/TiuShTf3ehYZi/200w.webp?cid=ecf05e47que9vt3vog4ikkkagez" \
               "sp6a7ltottn47qq0ug4cd&rid=200w.webp&ct=g' width='400'>"
    elif guess < rand_number:
        return "<p style='color:blue;font-size:50px'>Too low!</p>" \
               "<img src='https://media2.giphy.com/media/3ov9jRPMChw9ZzVlUk/200w.webp?cid=ecf05e47abhajr8xt5mp7n" \
               "ivw65a5n578jblfkllyjlc0151&rid=200w.webp&ct=g' width='400'>"
    else:
        return "<p style='color:green;font-size:50px'>You are right!</p>" \
               "<img src='https://media2.giphy.com/media/4Zo41lhzKt6iZ8xff9/giphy.webp?cid=ecf05e47pf2270pfn2tt5" \
               "dh0e51gju6g2kfnz5qyx8mpql53&rid=giphy.webp&ct=g' width='400'>"


if __name__ == "__main__":
    app.run(debug=True)