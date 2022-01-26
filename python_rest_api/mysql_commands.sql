CREATE TABLE `employee_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `address` text DEFAULT NULL,
  PRIMARY KEY (`id`)
)
;

INSERT INTO employee_details(name, email, phone, address) VALUES('Alex', 'alex@testapi.com', '1234567890', 'London');
INSERT INTO employee_details(name, email, phone, address) VALUES('Bob', 'bob@testapi.com', '0987654321', 'USA');
INSERT INTO employee_details(name, email, phone, address) VALUES('Roy', 'roy@testapi.com', '1357924680', 'India');
