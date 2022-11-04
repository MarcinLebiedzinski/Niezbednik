# Relacja jeden do wielu pomiędzy book(book_id, isbn, name, description, is_loaned)a authors (author_id, name)
# Należy stworzyć w book kolumnę author_id, wpisać odpowiednie wartości i ustawic relację

add_column_author_id = "ALTER TABLE	book ADD author_id int NOT NULL;"
update_column = "UPDATE book SET author_id=5 WHERE book_id=10;"
set_references = "ALTER TABLE	book ADD FOREIGN KEY(author_id) REFERENCES authors(author_id);"

# Relacja wielu do wielu book i category
# należy stworzyć dodatkową tabelę gdzie zbierzemy nr id książek i nr id categorii i uzupełnimy tą tabelę

add_table = """
CREATE TABLE bookcategory(
id serial,
book_id int NOT NULL,
category_id int NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (book_id) REFERENCES book(book_id),
FOREIGN KEY (category_id) REFERENCES category(category_id)
);
"""
fill_table = """
SELECT * FROM bookcategory;
INSERT INTO bookcategory(book_id, category_id) VALUES (1, 1);
INSERT INTO bookcategory(book_id, category_id) VALUES (2, 2);
INSERT INTO bookcategory(book_id, category_id) VALUES (3, 1);
INSERT INTO bookcategory(book_id, category_id) VALUES (4, 1);
INSERT INTO bookcategory(book_id, category_id) VALUES (5, 1);
INSERT INTO bookcategory(book_id, category_id) VALUES (6, 1);
INSERT INTO bookcategory(book_id, category_id) VALUES (7, 3);
INSERT INTO bookcategory(book_id, category_id) VALUES (8, 4);
INSERT INTO bookcategory(book_id, category_id) VALUES (9, 3);
INSERT INTO bookcategory(book_id, category_id) VALUES (10, 3);
"""

join tables = """
SELECT * FROM book 
JOIN bookcategory 
ON book.book_id = bookcategory.book_id
JOIN category
ON bookcategory.category_id = category.category_id;
"""

# Relacja wielu do wielu client i book
add_table2 = """
CREATE TABLE bookclient(
id serial,
book_id int NOT NULL,
client_id int NOT NULL,
loan_date date DEFAULT NULL,
return_date date DEFAULT NULL,
PRIMARY KEY (id),
FOREIGN KEY (book_id) REFERENCES book(book_id),
FOREIGN KEY (client_id) REFERENCES client(client_id)
);
"""


join_table2 = """
SELECT * FROM book 
JOIN bookclient 
ON book.book_id = bookclient.book_id
JOIN client
ON bookclient.client_id = client.client_id;

"""