CREATE DATABASE carles_database;

CREATE USER 'python'@'localhost' IDENTIFIED BY 'blog.carlesmateo.com-db-password';
CREATE USER 'python'@'%' IDENTIFIED BY 'blog.carlesmateo.com-db-password';
GRANT ALL PRIVILEGES ON carles_database.* TO 'python'@'localhost';
GRANT ALL PRIVILEGES ON carles_database.* TO 'python'@'%';

USE carles_database;

CREATE TABLE car_queue (
    i_id_car int,
    s_model_code varchar(25),
    s_color_code varchar(25),
    s_extras varchar(100),
    i_right_side int,
    s_city_to_ship varchar(25)
);

INSERT INTO car_queue (i_id_car, s_model_code, s_color_code, s_extras, i_right_side, s_city_to_ship) VALUES (1, "Golf 6", "Silberweiß", "2WD, GPS, MULTIMEDIA_V3", 0, "Wolfsburg");
INSERT INTO car_queue (i_id_car, s_model_code, s_color_code, s_extras, i_right_side, s_city_to_ship) VALUES (2, "Mercedes Benz A 2021", "Midnightblack", "COND_AIR, GPS, MULTIMEDIA_V3, SECURITY_V5", 0, "Weinheim");
INSERT INTO car_queue (i_id_car, s_model_code, s_color_code, s_extras, i_right_side, s_city_to_ship) VALUES (2, "Ford Ka 2009", "White", "FUEL_EFF_V3", 0, "Seckenheim");