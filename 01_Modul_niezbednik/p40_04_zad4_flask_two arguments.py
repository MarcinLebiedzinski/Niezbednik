from flask import Flask

app = Flask(__name__)

@app.route('/licz/<int:liczba1>/<int:liczba2>')
def showtime(liczba1, liczba2):
    multiply = liczba1 * liczba2
    return f"{multiply}"

if __name__ == "__main__":
    app.run(debug=True)