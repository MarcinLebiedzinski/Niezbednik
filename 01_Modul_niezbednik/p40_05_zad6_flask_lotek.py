from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/lotek/')
def showtime():
    lista = list(range(1, 50))
    lista2 = []
    if request.method == 'GET':
        for i in range(6):
            random.shuffle(lista)
            random_number = lista.pop(0)
            lista2.append(random_number)
        return f"{lista2}"
    else:
        return "POST METHOD"

if __name__ == "__main__":
    app.run(debug=True)