from flask import Flask, request

app = Flask(__name__)


def html_start(min_value, max_value, amount_of_tries):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head<
        <meta charset="UTF-8">
        <title> Game guess the number! </title>
    </head>
    <body>
    <h1> Imagine the number from 0 to 1000 and I will guess it in max 10 steps </h1>
    <h1> If You are ready, please click START </h1>
    <form action="" method="POST">
        <input type="submit" name="button" value="START"></input>
        <input type="hidden" name="min" value="{min_value}"></input>
        <input type="hidden" name="max" value="{max_value}"></input>
        <input type="hidden" name="tries" value="{amount_of_tries}"></input>
    </form>
    </body>
    </html>   
    """


def html_game(guess_number, min_value, max_value, amount_of_tries):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head<
        <meta charset="UTF-8">
        <title> Game guess the number! </title>
    </head>
    <body>
    <h1> My {amount_of_tries} choice. The number You're imagine is {guess_number} </h1>
    <form action="" method="POST">
 
        <label for="choice">Choose answer: </label>
        <select name="button" id="button">
            <option value="too_big">Too big!</option>
            <option value="too_small">Too small!</option>
            <option value="you_won" selected>You won!</option>
        </select>
  
        <input type="submit" value="Send"></input>
        
        <input type="hidden" name="min" value="{min_value}"></input>
        <input type="hidden" name="max" value="{max_value}"></input>
        <input type="hidden" name="tries" value="{amount_of_tries}"></input>
    </form>
    </body>
    </html>   
"""


def html_win():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head<
        <meta charset="UTF-8">
        <title> Game guess the number! </title>
    </head>
    <body>
    <h1> I won! Thank You for the game! </h1>
    </body>
    </html>   
"""


@app.route("/guessgame", methods=["GET", "POST"])
def guessgame():

    if request.method == "GET":
        min = 0
        max = 1000
        tries = 0
        return html_start(min, max, tries)
    else:
        button = request.form["button"]
        min = int(request.form["min"])
        max = int(request.form["max"])
        tries = int(request.form["tries"])
        guess = int((max - min) / 2) + min
        if button == 'START':
            tries += 1
            return html_game(guess, min, max, tries)
        elif button == 'you_won':
            return html_win()
        elif button == 'too_big':
            max = guess
            guess = int((max - min) / 2) + min
            tries += 1
            return html_game(guess, min, max, tries)
        elif button == 'too_small':
            min = guess
            guess = int((max - min) / 2) + min
            tries += 1
            return html_game(guess, min, max, tries)


if __name__ == "__main__":
    app.run(debug=True)