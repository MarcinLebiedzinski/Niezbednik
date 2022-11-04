
from flask import Flask, request
import random

rand_number = random.randint(1, 10)

app = Flask(__name__)


def html_start(rand_number, tries):
    return f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title> Take Your Chance! Are You Winner or Looser? </title>
    </head>
    <body>
    <h1> Guess the number form 1 to 10 </h1>
    <form action="" method="POST">
        <label> Input number : </label><br>
        <input type="text" name="user_number"></input><br>
        <br><input type="submit" value="Check"></input><br>
        <input type="hidden" name="guess" value="{rand_number}"></input>
        <input type="hidden" name="tries" value="{tries}"></input>
    </form>
    </body>
    </html>   
    """


def html_win(tries):
    return f"""
    <html>
    <head<
        <meta charset="UTF-8">
        <title> Take Your Chance! Are You Winner or Looser? </title>
    </head>
    <body>
    <h1> Congratulation!!! You are winner! You hit with {tries} times! </h1>
    </body>
    </html>
    """


def html_greater(rand_number, tries):
    return f"""
    <html>
    <head<
        <meta charset="UTF-8">
        <title> Take Your Chance! Are You Winner or Looser? </title>
    </head>
    <body>
    <h1> Nop! Try again! Number is greater </h1>
    <form action="" method="POST">
        <label> Input number: </label><br>
        <input type="text" name="user_number"></input><br>
        <br><input type="submit" value="Check"></input><br>
        <input type="hidden" name="guess" value="{rand_number}"></input>
        <input type="hidden" name="tries" value="{tries}"></input>        
    </body>
    </html>
    """


def html_smaller(rand_number, tries):
    return f"""
    <html>
    <head<
        <meta charset="UTF-8">
        <title> Take Your Chance! Are You Winner or Looser? </title>
    </head>
    <body>
    <h1> Nop! Try again! Number is smaller </h1>
    <form action="" method="POST">
        <label> Input number: </label><br>
        <input type="text" name="user_number"></input><br>
        <br><input type="submit" value="Check"></input><br>
        <input type="hidden" name="guess" value="{rand_number}"></input>
        <input type="hidden" name="tries" value="{tries}"></input>        
    </body>
    </html>
    """


@app.route("/guessgame", methods=["GET", "POST"])
def guess():
    tries = 1
    if request.method == "GET":
        return html_start(rand_number, tries)
    else:
        user_num = int(request.form["user_number"])
        computer_number = int(request.form["guess"])
        tries = int(request.form["tries"])
        if computer_number == user_num:
            return html_win(tries)
        elif computer_number > user_num:
            tries += 1
            return html_greater(computer_number, tries)
        else:
            tries +=1
            return html_smaller(computer_number, tries)


if __name__ == "__main__":
    app.run(debug=True)
