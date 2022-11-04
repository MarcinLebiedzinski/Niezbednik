from typing import Optional
from psycopg2 import connect, OperationalError
from psycopg2.errors import UndefinedTable
from flask import Flask, request


def execute_sql(sql_to_execute: str) -> Optional[list]:
    try:
        conn = connect(user='postgres',
                       password='coderslab',
                       host='localhost',
                       database='library_db')
        with conn.cursor() as cur: #Ta składnia pozwala na nie używanie commit, tutaj jednak ją dajemy dla dobrej praktyki
            cur.execute(sql_to_execute)
            conn.commit() # zatwierdza transakcje (gdyby było więcej operacji do wykonania to dopiero tutaj jest zamknięcie), jak ustawimy na conn.commit = True to wyłączymy transakcje
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


def html_add_book():
    return f"""
            <form class="book_form" method="post" action="#">
                <label>ISBN</label><br>
                <input name="isbn" type="text" maxlength="255" value=""/><br>
                
                <label>Book name</label><br>
                <input name="book_name" type="text" maxlength="255" value=""/><br>
                
                <label>Description</label><br>
                <input name="desc" type="text" maxlength="255" value=""/><br>
                
                <label>Author name</label><br>
                <input name="author_name" type="text" maxlength="255" value=""/><br>
                                
                <button type="submit" name="submit" value="movie">Submit</button>
            </form>
    """


def html_add_client():
    return f"""
            <form class="client_form" method="post" action="#">
                <label>first name</label><br>
                <input name="first_name" type="text" maxlength="255" value=""/><br>

                <label>last name</label><br>
                <input name="last_name" type="text" maxlength="255" value=""/><br>

                <button type="submit" name="submit" value="movie">Submit</button>
            </form>
    """


def html_loan(list_of_book):
    return f"""
            <HTML>
            <HEAD> Below list of books: </HEAD><BR>
            <HEAD>{list_of_book}</HEAD><BR>
            <HEAD></HEAD><BR>
            <HEAD> Please input data to loan book: </HEAD>
                        
            <form class="client_form" method="post" action="#">
                <label>client id</label><br>
                <input name="client_id" type="number" maxlength="255" value=""/><br>
                           
                <label>book id</label><br>
                <input name="book_id" type="text" maxlength="255" value=""/><br>

                <label>loan date</label><br>
                <input name="loan_date" type="date" value=""/><br>

                <label>return date</label><br>
                <input name="return_date" type="date" value=""/><br>

                <button type="submit" name="submit" value="movie">Submit</button>
            </form>
    """


app = Flask(__name__)


@app.route("/books")
def get_books():
        result_book_list = ""
        sql_code = f"SELECT * FROM book;"
        books_list = execute_sql(sql_code)
        for book in books_list:
            result_book_list += f"<BR> Book's id: {book[0]}, book's name: {book[2]}, isbn: {book[1]}\n"

        return f"""
        <HTML>
        Below list of books:
        {result_book_list}
        </HTML>
        """


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "GET":
        return html_add_book()
    else:
        book_name = request.form["book_name"]
        desc = request.form["desc"]
        isbn = request.form["isbn"]
        author_name = request.form["author_name"]
        authors_info = execute_sql("SELECT * FROM authors;")
        author_list = [author[1] for author in authors_info]
        if author_name not in author_list:
            sql_code = f"INSERT INTO authors (name) VALUES ('{author_name}');"
            execute_sql(sql_code)
            sql_code = f"SELECT * FROM authors WHERE name = '{author_name}';"
            row = execute_sql(sql_code)
            _id = row[0][0]
            sql_code = f"INSERT INTO book (isbn, name, description, author_id) VALUES ('{isbn}', '{book_name}', '{desc}', '{_id}');"
            execute_sql(sql_code)
            return f"""
                <html>
                Book: {book_name} has been added to data base library_db with description: '{desc}' and isbn {isbn}.
                </html>
                """
        else:
            sql_code = f"SELECT * FROM authors WHERE name = '{author_name}';"
            row = execute_sql(sql_code)
            _id = row[0][0]
            sql_code = f"INSERT INTO book (isbn, name, description, author_id) VALUES ('{isbn}', '{book_name}', '{desc}', '{_id}');"
            execute_sql(sql_code)
            return f"""
                <html>
                Book: {book_name} has been added to data base library_db with description: '{desc}' and isbn {isbn}.
                </html>
                """


@app.route("/book_details/<book_id>")
def print_book_detail(book_id):
        try:
            sql_code = f"SELECT * FROM book WHERE book_id={book_id};"
            book = execute_sql(sql_code)[0]
            return f"""
            <HTML> Details of selected book below:
            <br> Book's id: {book[0]}
            <br> book's name: {book[2]}
            <br> isbn: {book[1]}
            <br> description: {book[3]}
            <br> is loaned: {book[4]}
            </HTML>
            """
        except:
            print("Invalid id")


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
        try:
            sql_code = f"DELETE FROM book WHERE book_id={book_id};"
            execute_sql(sql_code)
            return f"Book with id: {book_id} has been deleted"
        except:
            print("Invalid id")


@app.route("/clients")
def get_clients():
        clients_list = ""
        sql_code = f"SELECT * FROM client;"
        clients = execute_sql(sql_code)
        for client in clients:
            clients_list += f"<BR> Client id: {client[0]}, name: {client[1]}, surname: {client[2]}\n"

        return f"""
        <HTML>
        Below list clients:
        {clients_list}
        </HTML>
        """


@app.route("/add_client", methods=["GET", "POST"])
def add_client():
    if request.method == "GET":
        return html_add_client()
    else:
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        sql_code = f"INSERT INTO client (first_name, last_name) VALUES ('{first_name}', '{last_name}');"
        execute_sql(sql_code)
        return f"Client has been added"


@app.route("/delete_client/<client_id>")
def delete_client(client_id):
        try:
            sql_code = f"DELETE FROM client WHERE client_id={client_id};"
            execute_sql(sql_code)
            return f"client with id: {client_id} has been deleted"
        except:
            print("Invalid id")


@app.route("/client_details/<client_id>")
def print_client_details(client_id):
        try:
            sql_code = f"SELECT * FROM client WHERE client_id={client_id};"
            client = execute_sql(sql_code)[0]
            client_info = f"""            
            <HTML> Client Info:
            <br> client id: {client[0]}
            <br> first name: {client[1]}
            <br> last name: {client[2]}
            <br>
            </HTML>
            """
            loaned_book = ""

            sql_code = f"SELECT * FROM bookclient WHERE client_id={client_id};"
            books = execute_sql(sql_code)
            if books:
                for book in books:
                    loaned_book += f"<HTML> Loaned Book id: {book[1]}, loan date: {book[3]}, return date: {book[4]}"
                return client_info + loaned_book
            else:
                return client_info + "Client didn't loan any book"
        except:
            print("Invalid id")



@app.route("/loan", methods=["GET", "POST"])
def loan():
    if request.method == "GET":
        result_book_list = ""
        sql_code = f"SELECT * FROM book;"
        books_list = execute_sql(sql_code)
        for book in books_list:
            result_book_list += f"<BR> Book's id: {book[0]}, book's name: {book[2]}, isbn: {book[1]}\n"
        return html_loan(result_book_list)
    else:
        client_id = request.form["client_id"]
        book_id = request.form["book_id"]
        loan_date = request.form["loan_date"]
        return_date = request.form["return_date"]

# dodanie do bookclient nowej pozycji
        sql_code = f"""
        INSERT INTO bookclient (book_id, client_id, loan_date, return_date) 
        VALUES ('{book_id}', '{client_id}', '{loan_date}', '{return_date}')
        ;"""
        execute_sql(sql_code)
        sql_code = f"UPDATE book SET is_loaned=TRUE WHERE book_id='{book_id}';"
        execute_sql(sql_code)
        return "Book is added to client's account. Book and bookclient have beed updated"

# sprawdzić czy w danych klienta pojawia się książka


        # return f"Client has been added"


if __name__ == "__main__":
    app.run(debug=True)
