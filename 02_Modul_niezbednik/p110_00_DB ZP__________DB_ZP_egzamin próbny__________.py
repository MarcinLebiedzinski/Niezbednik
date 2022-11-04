# psql -h localhost -U postgres -W -d postgres

create_database = "CREATE DATABASE temp_database;"

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
item_id int NOT NULL,
order_id int NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (item_id) REFERENCES Items(id) ON DELETE CASCADE,
FOREIGN KEY (order_id) REFERENCES Orders(id) ON DELETE CASCADE
);
"""

query_5_alternatywnie = """
CREATE TABLE ItemsOrders(
id serial PRIMARY KEY,
item_id int REFERENCES Items (id) ON DELETE CASCADE,
order_id int REFERENCES Orders (id) ON DELETE CASCADE
"""

insert_users = """
INSERT INTO Users (name, email, PASSWORD)
VALUES 
('Jan Nowak', 'jan.nowak@gmail.com', 'jannowak123'),
('Andrzej Duda', 'andrzej.duda@gmail.com', 'andrzejduda123'),
('Leszek Kowalski', 'leszek.kowalski@gmail.com', 'leszekkowalski123'),
('Pankracy Psikuta', 'pankracy.psikuta@gmail.com', 'pankracypsikuta123');
"""

insert_messages = """
INSERT INTO Messages (user_id, message)
VALUES 
(1, 'Cześć jestem Jan Kowalski'),
(2, 'Cześć jestem Andrzej Duda'),
(3, 'Cześć jestem Leszek Kowalski'),
(4, 'Cześc jestem Pankracy Psikuta');
"""

insert_items = """
INSERT INTO Items (name, description, price)
VALUES 
('mydło szare', 'pieni się', 3.5),
('szampon', 'przeciwłupieżowy', 12),
('gazeta', 'najświeższe informacje', 4.55),
('chipsy', 'paprykowe', 5.22);
"""

insert_orders = """
INSERT INTO Orders (description)
VALUES 
('Zamówienie nr 1'),
('Zamówienie nr 2'),
('Zamówienie nr 3'),
('Zamówienie nr 4');
"""

insert_itemsorders = """
INSERT INTO ItemsOrders (item_id, order_id)
VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4);
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

query_10 = "ALTER TABLE Messages ADD date_of_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP;"

