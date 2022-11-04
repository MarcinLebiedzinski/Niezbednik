from flask import Flask, request
from math import factorial

app = Flask(__name__)

HTML_START = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head<
        <meta charset="UTF-8">
        <title> Flask math  </title>
    </head>
    <body>
    <h1> Flask math </h1>
    <form action="" method="POST">
        <label> Podaj liczbę naturalną: </label><br>
        <input type="text" name="number"></input><br>
        <input type="submit" value="Wyślij"></input>
    </form>
    </body>
    </html>   
    """


@app.route("/", methods=["GET", "POST"])
def math():
    if request.method == "GET":
        return HTML_START
    else:
        number = int(request.form["number"])
        return f"""
                    <!DOCTYPE html>
            <html lang="en">
            <head<
                <meta charset="UTF-8">
                <title> Flask math  </title>
            </head>
            <table>
              <tbody>
                <tr>
                  <th>Działanie</th>
                  <th>Wynik</th> 
                <tr>
                  <td>2 do potęgi n</td>
                  <td>{2 ** number}</td>
                </tr>
                <tr>
                  <td>n do potęgi n</td>
                  <td>n{number ** number}</td>
                </tr>
                <tr>
                  <td>n silnia</td>
                  <td>{factorial(number)}</td>
                </tr>
              </tbody>
            </table>
            </html>     
            """


if __name__ == "__main__":
    app.run(debug=True)
