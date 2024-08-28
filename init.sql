USE ziptie;
DROP TABLE IF EXISTS owners;

CREATE TABLE owners (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    last_name VARCHAR(60) NOT NULL,
    email VARCHAR(120)
);

INSERT INTO owners (name, last_name, email) VALUES
('John', 'Doe', 'john.doe@example.com'),
('Jane', 'Smith', 'jane.smith@example.com'),
('Emily', 'Johnson', 'emily.johnson@example.com'),
('Michael', 'Brown', 'michael.brown@example.com');


DROP TABLE IF EXISTS cars;

CREATE TABLE cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(20) NOT NULL,
    model VARCHAR(30) NOT NULL,
    production_date DATE,
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES owners(id)
);

INSERT INTO cars (brand, model, production_date, owner_id) VALUES
('Ferrari', 'LaFerrari', '2015-03-15', 1),
('Lamborghini', 'Aventador SVJ', '2020-07-22', 1),
('McLaren', 'P1', '2016-11-05', 1),
('Porsche', '918 Spyder', '2016-04-30', 1);

INSERT INTO cars (brand, model, production_date, owner_id) VALUES
('Bugatti', 'Chiron', '2018-05-10', 2),
('Pagani', 'Huayra', '2019-09-12', 2),
('Aston Martin', 'Vulcan', '2021-01-20', 2);

INSERT INTO cars (brand, model, production_date, owner_id) VALUES
('Koenigsegg', 'Agera RS', '2018-03-25', 3);