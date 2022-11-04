
from flask import Flask
app = Flask(__name__)


@app.route('/hello/<name>', methods=['GET', 'POST'])
def hello(name):
    if request.method == 'GET':
        return f"Hello {name}!"
    else:
        return "POST METHOD"


@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return f"{result}"


if __name__ == "__main__":
    app.run(debug=True)

# Program tworzący serwer
# funckja hello musi zwracać stringa
# Dekorator argumentem jest ścieżka gdzie będzie widoczny (strona główna)
# if __name__ == "__main__" Uruchom poniższy run jeśli odpalamy ten plik (można np. odpalić funkcję z innego pliku) - nie odpalić czegoś z innego pliku z biblioteką
# (debug=True) -
# endpoint /pudelek/kufelek
# Magiczna metoda name (stała wymagana przez Flask)

# ręcznie w przeglądarce trzeba dopisać parametry /hello/imie
# narzędzia do metody której metody używamy (np. boomerang)