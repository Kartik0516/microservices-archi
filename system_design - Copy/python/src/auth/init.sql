CREATE USER 'Kartikay0516'@'localhost' IDENTIFIED BY 'kartik123';

CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

USE auth;

CREATE TABLE user (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);

INSERT INTO user (email, password) VALUES ('sethkartikay59@gmail.com', '89Kr@#123');
SHOW variables like 'port'
  