USE botanical_garden;
CREATE TABLE Plants
(plant_type_ID INT NOT NULL PRIMARY KEY,
plant_type CHAR(15) NOT NULL UNIQUE,
quantity_in_stock INT,
cost_per_plant INT);


