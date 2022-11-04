from flask import Flask, request

app = Flask(__name__)

def html_start():
    return """
           <form action="" method="POST">
               <label>Liczba1:</label>
               <input type="number" name="liczba1"><br><br>

               <label>Liczba2:</label>
               <input type="number" name="liczba2"><br><br>

               <label for="dzialanie">Wybierz działanie</label>
                   <select name='dzialanie' id='dzialanie'>
                   <option value="dodawanie">+</option>
                   <option value="odejmowanie">-</option>
                   <option value="mnozenie">*</option>
                   <option value="dzielenie">/</option>
                   </select><br><br>

               <input type="submit" value="Wyślij">
           </form>  
    """


@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    if request.method == "GET":
        return html_start()
    else:
        number1 = request.form["liczba1"]
        number2 = request.form["liczba2"]
        akcja = request.form["dzialanie"]
        if akcja == "dodawanie":
            return f"{float(number1) + float(number2)}"
        elif akcja == "odejmowanie":
            return f"{float(number1) - float(number2)}"
        elif akcja == "mnozenie":
            return f"{float(number1) * float(number2)}"
        else:
            try:
                return f"{float(number1) / float(number2)}"
            except ZeroDivisionError:
                return f" Nie wolno dzielić przez 0"


if __name__ == "__main__":
    app.run(debug=True)