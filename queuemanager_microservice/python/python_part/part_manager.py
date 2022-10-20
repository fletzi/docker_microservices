import mysql.connector

# Verbindung zur Datenbank
try:
    connection = mysql.connector.connect(user='root', password='root', host='mysql_part', port='3306',database='db_part')
    print("▣ Datenbankverbindung erfolgreich hergestellt")
except mysql.connector.Error as err:
    print("▣ Datenbank fährt noch hoch...")


# Ausgabe aller Elemente der Tabelle car_part (Lager)
def get_all_parts():
    cursor = connection.cursor()
    cursor.execute('Select * FROM car_part')
    car_part = cursor.fetchall()
    print()
    print("| ID | Name | Menge | Lagerort |")
    for i in car_part:
        print(i)

    print()
    input("▨ Enter - zurück zum Hauptmenü: ")
    print()


# Liefert Element der Tabelle car_part mit der übergebenen ID
def get_part_by_id(i_id_part):
    cursor = connection.cursor()
    cursor.execute('Select * FROM car_part WHERE i_id_part =' + i_id_part)
    car_part = cursor.fetchall()

    if len(car_part) == 0:
        print("▣ Kein passender Eintrag gefunden!")
        input("▨ Enter - zurück zum Hauptmenü: ")
        return

    print(car_part)
    input("▨ Enter - zurück zum Hauptmenü: ")
    return car_part


# Überprüft die übergebene ID auf Eingabefehler
def take_part_id(s_option):
    i_id_part = input("▨ ID eingeben › ")

    if i_id_part == "":
        print("▣ Eingabe ist leer!")
        input("▨ Enter - zurück zum Hauptmenü: ")
        return

    if not i_id_part.isdigit():
        print("▣ Eingabe ist nicht nummerisch!")
        input("▨ Enter - zurück zum Hauptmenü: ")
        return

    if int(i_id_part) <= 0:
        print("▣ ID muss größer 0 sein!")
        input("▨ Enter - zurück zum Hauptmenü: ")
        return

    if s_option == "1":
        validate_id(i_id_part)

    if s_option == "3":
        get_part_by_id(i_id_part)

    if s_option == "4":
        exists_id(i_id_part)


# Gibt die part_amount des Elements mit der ID i_id_part in der Tabelle car_part aus
def get_part_amount(i_id_part):
    cursor = connection.cursor()
    cursor.execute('Select i_part_amount FROM car_part WHERE i_id_part =' + i_id_part)
    car_part = cursor.fetchall()

    id_list = ["%s" % x for x in car_part]

    for i in id_list:
        car_amount = int(i)

    if len(car_part) == 0:
        print("▣ Kein passender Eintrag gefunden!")
        input("▨ Enter - zurück zum Hauptmenü: ")
        return

    return car_amount


# Löscht oder dekrementiert part_amount der Tabelle car_part
def delete_part_by_id(i_id_part):
    i_max_amount = int(get_part_amount(i_id_part))
    print("▨ Maximale Menge zum Ausbuchen: " + str(i_max_amount))
    s_amount = input("▨ Wie viel wollen Sie ausbuchen: ")

    if int(s_amount) > i_max_amount:
        print("▣ So viel ist nicht auf Lager!")
        delete_part_by_id(i_id_part)
        return
    if int(s_amount) == i_max_amount:
        s_delete = input("▨ Wollen Sie die Teile wirklich AUSBUCHEN. Geben Sie Y/y zum ausbuchen ein: ")
        if s_delete.upper() == "Y":
            cursor = connection.cursor()
            cursor.execute('DELETE FROM car_part WHERE i_id_part =' + str(i_id_part))

            print("▣ Teile erfolgreich ausgebucht")
            input("▨ Enter - zurück zum Hauptmenü: ")
            return

    new_amount = i_max_amount - int(s_amount)
    s_delete = input("▨ Wollen Sie die Teile wirklich AUSBUCHEN. Geben Sie Y/y zum ausbuchen ein: ")
    if s_delete.upper() == "Y":
        cursor = connection.cursor()
        sql = "UPDATE car_part SET i_part_amount = " + str(new_amount) + " WHERE i_id_part =" + str(i_id_part)
        cursor.execute(sql)

        print("▣ Teile erfolgreich ausgebucht")
        input("▨ Enter - zurück zum Hauptmenü: ")
        return


# Fügt der Tabelle car_part ein neues Element hinzu
def add_part(i_id_part):
    s_part_name = input("▨ Teilname eingeben: ")
    i_part_amount = input("▨ Menge eingeben: ")
    if i_part_amount == "" or int(i_part_amount) <= 0:
        print("▣ Menge darf nicht leer oder negativ sein!")
        add_part(i_id_part)
        return
    s_part_warehouse = input("▨ Lagerort eingeben: ")
    cursor = connection.cursor()
    sql = "INSERT INTO car_part (i_id_part, s_part_name, i_part_amount, s_part_warehouse) VALUES (%s, %s, %s, %s)"
    val = (i_id_part, s_part_name, int(i_part_amount), s_part_warehouse)
    cursor.execute(sql, val)

    cursor.execute('Select * FROM car_part WHERE i_id_part =' + i_id_part)
    new_part = cursor.fetchall()
    print("▣ Neues Teil erfolgreich hinzugefügt")
    print(new_part)
    input("▨ Enter - zurück zum Hauptmenü: ")


# Überprürft ob die übergebene ID in der Tabelle car_part enthalten ist
def validate_id(i_id_part):
    cursor = connection.cursor()
    cursor.execute('Select i_id_part FROM car_part')
    car_part = list(cursor.fetchall())

    id_list = ["%s" % x for x in car_part]

    if i_id_part in id_list:
        print("▣ ID bereits vergeben!")
        take_part_id("1")
        return

    add_part(i_id_part)


# Überprüft ob die übergebne ID in der Tablle car_part nicht enthalten ist
def exists_id(i_id_part):
    cursor = connection.cursor()
    cursor.execute('Select i_id_part FROM car_part')
    car_part = list(cursor.fetchall())

    id_list = ["%s" % x for x in car_part]

    if i_id_part not in id_list:
        print("▣ ID nicht vorhanden!")
        take_part_id("4")
        return

    delete_part_by_id(i_id_part)


# Stellt das Hauptmenü dar
def main_menu():
    # Hauptmenü
    while True:
        print("")
        print("• Hauptmenü Lager •")
        print("")
        print("▣ [1] Teil zum Lager hinzufügen")
        print("▣ [2] Lager ausgeben")
        print("▣ [3] Teil über ID ausgeben")
        print("▣ [4] Teil über ID ausbuchen")
        print("")
        print("▣ [0] Menü Verlassen")
        print("")

        s_option = input("▨ Option wählen › ")
        if s_option == "1":
            take_part_id(s_option)
        if s_option == "2":
            get_all_parts()
        if s_option == "3":
            take_part_id(s_option)
        if s_option == "4":
            take_part_id(s_option)

        if s_option == "0":
            exit()


main_menu()