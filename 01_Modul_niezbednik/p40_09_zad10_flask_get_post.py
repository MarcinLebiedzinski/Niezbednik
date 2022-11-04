from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        return "Wysłałeś POST"
    else:
        return "Wysłałeś GET"


if __name__ == "__main__":
    app.run(debug=True)



# curl --request POST http://localhost:5000/ - zapytanie POST
# curl --request GET http://localhost:5000/ - zapytanie GET