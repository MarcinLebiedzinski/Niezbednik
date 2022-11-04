from typing import Optional
from psycopg2 import connect, OperationalError
from psycopg2.errors import UndefinedTable
from flask import Flask, request


app = Flask(__name__)


def execute_sql(sql_to_execute: str) -> Optional[list]:
    try:
        conn = connect(user='postgres',
                       password='coderslab',
                       host='localhost',
                       database='exam2')
        with conn.cursor() as cur:
            cur.execute(sql_to_execute)
            conn.commit() #
            try:
                result = list(cur)
            except:
                result = None
    except OperationalError:
        print('Nieudane połączenie z bazą danych.')
        result = None
    except UndefinedTable:
        print('Nie znaleziono tabeli.')
        result = None
    else:
        conn.close()

    return result


def html_add_product():
    return f"""
    <form class="book_form" method="post" action="#">
    <label>name</label><br>
    <input name="product_name" type="text" maxlength="255" value=""/><br>

    <label>Description</label><br>
    <input name="desc" type="text" maxlength="255" value=""/><br>

    <label>Price</label><br>
    <input name="price" type="text" value=""/><br>

         
    <br><input type="submit" value="Send"></input><br>
    """

@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "GET":
        return html_add_product()
    else:
        product_name = request.form["product_name"]
        desc = request.form["desc"]
        try:
            price = float(request.form["price"])
        except ValueError:
            return "Invalid data!"

        sql_code = f"INSERT INTO Items (name, description, price) VALUES ('{product_name}', '{desc}', '{price}');"
        execute_sql(sql_code)
        return "Product added"


if __name__ == "__main__":
    app.run(debug=True)