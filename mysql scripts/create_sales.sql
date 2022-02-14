USE botanical_garden;
CREATE TABLE Sales_Transaction 
(transaction_ID INT NOT NULL PRIMARY KEY,
plant_ID INT NOT NULL,
customer_ID INT NOT NULL,
employee_ID INT NOT NULL,
quantity_sold INT,
amount_received INT,
transaction_date DATE,
FOREIGN KEY (plant_ID) REFERENCES Plants(plant_type_ID),
FOREIGN KEY (customer_ID) REFERENCES Customers(customer_ID),
FOREIGN KEY (employee_ID) REFERENCES Employee(employee_ID));

