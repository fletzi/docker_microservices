import mysql.connector

# Verbindung zur Datenbank
try:
    connection = mysql.connector.connect(user='root', password='root', host='mysql_car', port='3306', database='db')
    print("▣ Datenbankverbindung erfolgreich hergestellt")
except mysql.connector.Error as err:
    print("▣ Datenbank fährt noch hoch...")


# Ausgabe aller Elemente der Tabelle car_queue (Warteschlange)
def get_all_cars():
    cursor = connection.cursor()
    cursor.execute('Select * FROM car_queue')
    car_queue = cursor.fetchall()
    print()
    print("| ID | Modellname | Farbe | Extras | Lieferort |")
    for i in car_queue:
        print(i)

    print()
    input("▨ Enter - zurück zum Hauptmenü: ")
    print()


# Liefert Element der Tabelle car_queue mit der übergebenen ID
def get_car_by_id(i_id_car):
    cursor = connection.cursor()
    cursor.execute('Select * FROM car_queue WHERE i_id_car =' + i_id_car)
    car_queue = cursor.fetchall()

    if len(car_queue) == 0:
        print("▣ Kein passender Eintrag gefunden!")
        input("▨ Enter - zurück zum Hauptmenü: ")
        return

    print(car_queue)
    input("▨ Enter - zurück zum Hauptmenü: ")
    return car_queue


# Überprüft die übergebene ID auf Eingabefehler
def take_car_id(s_option):
    i_id_car = input("▨ ID eingeben › ")

    if i_id_car == "":
        print("▣ Eingabe ist leer!")
        input("▨ Enter - zurück zum Hauptmenü: ")
        return

    if not i_id_car.isdigit():
        print("▣ Eingabe ist nicht nummerisch!")
        input("▨ Enter - zurück zum Hauptmenü: ")
        return

    if int(i_id_car) <= 0:
        print("▣ ID muss größer 0 sein!")
        input("▨ Enter - zurück zum Hauptmenü: ")
        return

    if s_option == "1":
        validate_id(i_id_car)

    if s_option == "3":
        get_car_by_id(i_id_car)

    if s_option == "4":
        exists_id(i_id_car)


# Löscht das Element der Tabelle car_queue mit der übergebenen ID 
def delete_car_by_id(i_id_car):
    s_delete = input("▨ Wollen Sie das Auto wirklich LÖSCHEN. Geben Sie Y/y zum löschen ein: ")
    if s_delete.upper() == "Y":
        cursor = connection.cursor()
        cursor.execute('DELETE FROM car_queue WHERE i_id_car =' + str(i_id_car))

        print("▣ Zeile(n) erfolgreich gelöscht")
        input("▨ Enter - zurück zum Hauptmenü: ")


# Fügt der Tabelle car_queue ein neues Element hinzu
def add_car(i_id_car):
    s_model_code = input("▨ Modellname eingeben: ")
    s_color_code = input("▨ Farbe eingeben: ")
    s_extras = input("▨ Extras eingeben: ")
    s_city_to_ship = input("▨ Lieferort eingeben: ")
    cursor = connection.cursor()
    sql = "INSERT INTO car_queue (i_id_car, s_model_code, s_color_code, s_extras, s_city_to_ship) VALUES (%s, %s, %s, %s, %s)"
    val = (i_id_car, s_model_code, s_color_code, s_extras, s_city_to_ship)
    cursor.execute(sql, val)

    cursor.execute('Select * FROM car_queue WHERE i_id_car =' + i_id_car)
    new_car = cursor.fetchall()
    print("▣ Neues Auto erfolgreich hinzugefügt")
    print(new_car)
    input("▨ Enter - zurück zum Hauptmenü: ")


# Überprürft ob die übergebene ID in der Tabelle car_queue enthalten ist
def validate_id(i_id_car):
    cursor = connection.cursor()
    cursor.execute('Select i_id_car FROM car_queue')
    car_queue = list(cursor.fetchall())

    id_list = ["%s" % x for x in car_queue]

    if i_id_car in id_list:
        print("▣ ID bereits vergeben!")
        take_car_id("1")
        return

    add_car(i_id_car)


# Überprüft ob die übergebne ID in der Tablle car_queue nicht enthalten ist
def exists_id(i_id_car):
    cursor = connection.cursor()
    cursor.execute('Select i_id_car FROM car_queue')
    car_queue = list(cursor.fetchall())

    id_list = ["%s" % x for x in car_queue]

    if i_id_car not in id_list:
        print("▣ ID nicht vorhanden!")
        take_car_id("4")
        return

    delete_car_by_id(i_id_car)


# Stellt das Hauptmenü dar
def main_menu():
    # Hauptmenü
    while True:
        print("")
        print("• Hauptmenü Warteschlange•")
        print("")
        print("▣ [1] Fahrzeug zur Warteschlange hinzufügen")
        print("▣ [2] Warteschlange ausgeben")
        print("▣ [3] Fahrzeug über ID ausgeben")
        print("▣ [4] Fahrzeug über ID aus Wartschelange löschen")
        print("")
        print("▣ [0] Menü Verlassen")
        print("")

        s_option = input("▨ Option wählen › ")
        if s_option == "1":
            take_car_id(s_option)
        if s_option == "2":
            get_all_cars()
        if s_option == "3":
            take_car_id(s_option)
        if s_option == "4":
            take_car_id(s_option)

        if s_option == "0":
            exit()


main_menu()
