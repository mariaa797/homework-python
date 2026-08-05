CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    publication_year INT NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

INSERT INTO books (title, author, publication_year, price)
VALUES
('Кобзар', 'Тарас Шевченко', 1840, 350.00),
('1984', 'Джордж Орвелл', 1949, 420.50),
('Майстер і Маргарита', 'Михайло Булгаков', 1967, 500.00),
('Гаррі Поттер і філософський камінь', 'Джоан Роулінг', 1997, 650.00);

UPDATE books
SET price = 450.00
WHERE id = 2;

DELETE FROM booksу
WHERE id = 3;