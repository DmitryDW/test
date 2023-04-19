CREATE TABLE book (
  id serial PRIMARY KEY,
  name varchar(255),
  author_id int
);

INSERT INTO book (name, author_id) VALUES ('The Great Gatsby', 1);

INSERT INTO book (name, author_id) VALUES ('Harry Potter', 3);

UPDATE book SET name = 'To Kill a Mockingbird' WHERE id = 2;

DELETE FROM book WHERE id = 3;

SELECT * FROM book;

SELECT * FROM book WHERE author_id = 3;

SELECT * FROM book WHERE name LIKE '%Harry Pott%';

SELECT * FROM book ORDER BY name ASC;

SELECT * FROM book JOIN author ON book.author_id = author.author_id;

CREATE TABLE author (author_id serial PRIMARY KEY, name varchar(255));

INSERT INTO author (name) VALUES ('Scott');

INSERT INTO author (name) VALUES ('Rouling');

INSERT INTO author (name) VALUES ('Bulgakov');