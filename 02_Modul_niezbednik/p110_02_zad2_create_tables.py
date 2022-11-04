create_database = "CREATE DATABASE exam2;"

query_1 = """
CREATE TABLE Users(
id serial,
name varchar(60),
email varchar(60) UNIQUE ,
password varchar(60),
PRIMARY KEY (id)
);
"""

query_2 = """
CREATE TABLE Messages(
id serial,
user_id int REFERENCES Users(id),
message text,
PRIMARY KEY (id)
);
"""

query_3 = """
CREATE TABLE Items(
id serial,
name varchar(40),
description text,
price decimal(7, 2),
PRIMARY KEY (id)
);
"""

query_4 = """
CREATE TABLE Orders(
id serial,
description text,
PRIMARY KEY (id)
);
"""

# Relacja wielu do wielu
query_5 = """
CREATE TABLE ItemsOrders(
id serial,
item_id int NOT NULL ON DELETE CASCADE,
order_id int NOT NULL ON DELETE CASCADE,
PRIMARY KEY (id),
FOREIGN KEY (item_id) REFERENCES Items(id),
FOREIGN KEY (order_id) REFERENCES Orders(id)
);
"""

query_5_alternatywnie = """
CREATE TABLE ItemsOrders(
id serial PRIMARY KEY,
item_id int REFERENCES Items (id) ON DELETE CASCADE,
order_id int REFERENCES Orders (id) ON DELETE CASCADE
"""

query_6 = "SELECT * FROM Items WHERE price>13;"

query_7 = "INSERT INTO Orders(description) VALUES('Przykładowy opis');"

query_8 = "DELETE FROM Users WHERE id=7;"

query_9 = """
SELECT * FROM Users 
JOIN Messages 
ON Users.id = messages.user_id;
"""
query_9_alternatywnie = """
SELECT Users.name AS user_name, Users.id AS user_id, Messages.message AS u_message
FROM Users JOIN Messages on Users.id=Messages.user_id
"""

query_10 = "ALTER TABLE Messages ADD column date_of_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP;"