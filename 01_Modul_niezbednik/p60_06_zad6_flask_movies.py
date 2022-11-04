from flask import Flask, request
from p60_70_exam import movies

app = Flask(__name__)


def html_start():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head<
        <meta charset="UTF-8">
        <title> movie </title>
    </head>
    <body>
    <h1> Hated or favourite movie ... Let's check </h1>
    <form action="" method="POST">
        <label> Enter movie title: </label><br>
        <input type="text" name="name_movie"></input><br>
        <input type="submit" value="Check"></input>
    </form>
    </body>
    </html>   
    """


def html_answer(answer):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head<
        <meta charset="UTF-8">
        <title> Result </title>
    </head>
    <body>
    <h1> {answer} </h1>
    </body>
    </html>   
"""


@app.route("/movies", methods=["GET", "POST"])
def guessgame():
    if request.method == "GET":
        return html_start()
    else:
        input_movie = request.form["name_movie"]
        if input_movie in movies['favourite']:
            return html_answer('Favourite!')
        elif input_movie in movies['hated']:
            return html_answer('Hated!')
        else:
            return html_answer('No such movie!')


if __name__ == "__main__":
    app.run(debug=True)
