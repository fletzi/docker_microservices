USE db_part;

CREATE TABLE car_part (
    i_id_part int,
    s_part_name varchar(25),
    i_part_amount int,
    s_part_warehouse varchar(25)
);

INSERT INTO car_part (i_id_part, s_part_name, i_part_amount, s_part_warehouse) VALUES (1, "Kupplung", 165, "Lager Nord");
INSERT INTO car_part (i_id_part, s_part_name, i_part_amount, s_part_warehouse) VALUES (2, "Frontscheibe", 33, "Lager Sued");
INSERT INTO car_part (i_id_part, s_part_name, i_part_amount, s_part_warehouse) VALUES (3, "Nockenwelle", 78, "Lager West");
INSERT INTO car_part (i_id_part, s_part_name, i_part_amount, s_part_warehouse) VALUES (4, "Dichtungsring", 3722, "Lager Sued");
INSERT INTO car_part (i_id_part, s_part_name, i_part_amount, s_part_warehouse) VALUES (5, "Motoroel", 294, "Lager Ost");