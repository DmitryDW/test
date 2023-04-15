CREATE TABLE book (
  id serial PRIMARY KEY,
  name varchar(255),
  author_id int
);

INSERT INTO book (name, author_id) VALUES ('The Great Gatsby', 1);

UPDATE book SET name = 'To Kill a Mockingbird' WHERE id = 2;

DELETE FROM book WHERE id = 3;

SELECT * FROM book;

SELECT * FROM book WHERE author_id = 4;

SELECT * FROM book WHERE name LIKE '%Harry Potter%';

SELECT * FROM book ORDER BY name ASC;

SELECT book.name, author.name FROM book JOIN author ON book.author_id = author.id;