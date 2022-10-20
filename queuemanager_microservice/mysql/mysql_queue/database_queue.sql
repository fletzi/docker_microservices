USE db;

CREATE TABLE car_queue (
    i_id_car int,
    s_model_code varchar(25),
    s_color_code varchar(25),
    s_extras varchar(100),
    s_city_to_ship varchar(25)
);

INSERT INTO car_queue (i_id_car, s_model_code, s_color_code, s_extras, s_city_to_ship) VALUES (1, "Golf 6", "Silberweiss", "2WD, GPS, MULTIMEDIA_V3", "Wolfsburg");
INSERT INTO car_queue (i_id_car, s_model_code, s_color_code, s_extras, s_city_to_ship) VALUES (2, "Mercedes Benz A 2021", "Midnightblack", "COND_AIR, GPS, MULTIMEDIA_V3, SECURITY_V5", "Weinheim");
INSERT INTO car_queue (i_id_car, s_model_code, s_color_code, s_extras, s_city_to_ship) VALUES (3, "Ford Ka 2009", "White", "FUEL_EFF_V3", "Seckenheim");