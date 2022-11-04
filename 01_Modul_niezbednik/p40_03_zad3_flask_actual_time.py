from flask import Flask
import datetime

app = Flask(__name__)

# @app.route('/hello/<name>', methods=['GET', 'POST'])
# def hello(name):
#     if request.method == 'GET':
#         return f"Hello {name}!"
#     else:
#         return "POST METHOD"

@app.route('/showtime')
def showtime():
    date_now = datetime.datetime.now()
    return f"aktualny czas to {date_now.strftime('%d/%m/%Y')}"

if __name__ == "__main__":
    app.run(debug=True)