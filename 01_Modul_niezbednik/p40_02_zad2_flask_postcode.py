from flask import Flask, request

app = Flask(__name__)

HTML_START = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head<
        <meta charset="UTF-8">
        <title> Flask postcode  </title>
    </head>
    <body>
    <h1> Flask postocde </h1>
    <form action="" method="POST">
        <label> Podaj kod: </label><br>
        <input type="text" name="code"></input><br>
        <input type="submit" value="Wyślij"></input>
    </form>
    </body>
    </html>   
    """


@app.route("/", methods=["GET", "POST"])
def post_code():
    if request.method == "GET":
        return HTML_START
    else:
        code = request.form["code"]
        code_list = code.split("-")
        try:
            if len(code_list) == 2 and isinstance(int(code_list[0]), int) and isinstance(int(code_list[1]), int) and (len(str(code_list[0])) == 2) and (len(str(code_list[1])) == 3):
                return f"Kod poprawny. Kod {code} jest zgodny z polskim formatem (00-001)"
            else:
                return f"Kod niepoprawny. Kod {code} nie jest zgodny zpolskim formatem (00-001)"
        except ValueError:
            return f"Kod niepoprawny. Kod {code} nie jest zgodny zpolskim formatem (00-001)"


if __name__ == "__main__":
    app.run(debug=True)