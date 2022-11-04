code = """
CREATE DATABASE library_db;

CREATE TABLE Authors
(
author_id serial,
name TEXT,
PRIMARY KEY (author_id)
);

CREATE TABLE Book
(
book_id serial,
ISBN varchar(13),
name varchar,
description TEXT,
is_loaned bool NOT NULL DEFAULT FALSE,
PRIMARY KEY (book_id)
);

CREATE TABLE Client
(
client_id serial,
first_name varchar,
last_name varchar,
PRIMARY KEY (client_id)
);

CREATE TABLE Category
(
category_id serial,
name varchar,
PRIMARY KEY (category_id)
);

INSERT INTO Authors (author_id, name)
VALUES (1, 'Stephen King'),
(2, 'Andrzej Sapkowski'),
(3, 'Rowling J.K.'),
(4, 'Coelho Paulo'),
(5, 'Brown Dan')
;

INSERT INTO Book (book_id, ISBN, name, description)
VALUES (1, 9780385121675, 'The Shining', 'horror'),
(2, 9783404130351, 'Cujo', 'thriller' ),
(3, 9780590353403, 'Harry Potter and the Philosopher’s Stone', 'fantasy'),
(4, 9788498387650, 'Harry Potter and the Chamber of Secrets', 'fantasy'),
(5, 9788493283612, 'Ostatnie Życzenie', 'fantasy'),
(6, 9788493283667, 'Miecz Przeznaczenia', 'fantasy'),
(7, 9780060825218, 'Zahir', 'novel'),
(8, 9788408052944, 'The Alchemist', 'novel'),
(9, 9780385513753, 'The da Vinci Code', 'mystery thriller'),
(10, 9780606304955, 'Angels and Demons', 'mystery thriller')
;

INSERT INTO Client (client_id, first_name, last_name)
VALUES (1, 'Jan', 'Nowak'),
(2, 'Donald', 'Trump'),
(3, 'Ewa', 'Chodakowska')
;

SELECT * FROM authors;

SELECT * FROM authors WHERE author_id = 2;

SELECT * FROM book;

SELECT * FROM book WHERE book_id = 2;

SELECT * FROM client;

SELECT * FROM client WHERE client_id = 1;

DELETE FROM book WHERE book_id = 5;
"""