from flask import Flask, request

app = Flask(__name__)


def html_hello():
    return """
    <HTML>
    <form action="" method="POST">
        <label> Imię: </label><br>
        <input type="text" name="user_name"></input><br>
        <label> Nazwisko: </label><br>
        <input type="text" name="user_surname"></input><br>
        <br><input type="submit" value="Wyślij"></input>
    </form>
    </HTML>    
    """


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return html_hello()
    else:
        user_name = request.form["user_name"]
        user_surname = request.form["user_surname"]
        return f"{hello} Witaj {user_name} {user_surname}"


if __name__ == "__main__":
    app.run(debug=True)