from lib.mysqllib import MySql
from do.cardo import CarDO


class QueueManager():

    def __init__(self, o_mysql):
        self.o_mysql = o_mysql

    def exit(self):
        exit(0)

    def main_menu(self):
        while True:
            print("┌─────────────────────────────────────────────────┐")
            print("│                   • Hauptmenü •                 │")
            print("├─────────────────────────────────────────────────┤")
            print("│                                                 │")
            print("│ [1] Fahrzeug zur Warteschlange hinzufügen       │")
            print("│ [2] Warteschlange ausgeben                      │")
            print("│ [3] Fahrzeug über ID ausgeben                   │")
            print("│ [4] Fahrzeug über ID aus Wartschelange löschen  │")
            print("├─────────────────────────────────────────────────┤")
            print("│ [0] Menü Verlassen                              │")
            print("└─────────────────────────────────────────────────┘")

            s_option = input("▨ Option wählen ›")
            if s_option == "1":
                self.add_new_car()
            if s_option == "2":
                self.see_all_cars()
            if s_option == "3":
                self.see_car_by_id()
            if s_option == "4":
                self.delete_by_id()

            if s_option == "0":
                self.exit()

    def get_all_cars(self):
        s_query = "SELECT * FROM car_queue"

        a_rows = self.o_mysql.query(s_query)
        a_o_cars = []

        for a_row in a_rows:
            i_id_car = a_row[0]
            s_model_code = a_row[1]
            s_color_code = a_row[2]
            s_extras = a_row[3]
            i_right_side = a_row[4]
            s_city_to_ship = a_row[5]

            o_car = CarDO(i_id_car=i_id_car, s_model_code=s_model_code, s_color_code=s_color_code, s_extras=s_extras, i_right_side=i_right_side, s_city_to_ship=s_city_to_ship)
            a_o_cars.append(o_car)

        return a_o_cars

    def get_car_by_id(self, i_id_car):
        b_success = False
        o_car = None

        s_query = "SELECT * FROM car_queue WHERE i_id_car=" + str(i_id_car)

        a_rows = self.o_mysql.query(s_query)

        if len(a_rows) == 0:
            # False, None
            return b_success, o_car

        i_id_car = a_rows[0][0]
        s_model_code = a_rows[0][1]
        s_color_code = a_rows[0][2]
        s_extras = a_rows[0][3]
        i_right_side = a_rows[0][4]
        s_city_to_ship = a_rows[0][5]

        o_car = CarDO(i_id_car=i_id_car, s_model_code=s_model_code, s_color_code=s_color_code, s_extras=s_extras, i_right_side=i_right_side, s_city_to_ship=s_city_to_ship)
        b_success = True

        return b_success, o_car

    def replace_apostrophe(self, s_text):
        return s_text.replace("'", "´")

    def insert_car(self, o_car):

        s_sql = """INSERT INTO car_queue 
                                (i_id_car, s_model_code, s_color_code, s_extras, i_right_side, s_city_to_ship) 
                         VALUES 
                                (""" + str(o_car.get_i_id_car()) + ", '" + o_car.get_s_model_code() + "', '" + o_car.get_s_color_code() + "', '" + o_car.get_s_extras() + "', " + str(o_car.get_i_right_side()) + ", '" + o_car.get_s_city_to_ship() + "');"

        i_inserted_row_count = self.o_mysql.insert(s_sql)

        if i_inserted_row_count > 0:
            print("■ ", i_inserted_row_count, " Zeile(n) eingefügt")
            b_success = True
        else:
            print("▣ Einfügen der Zeile ist Fehlgeschlagen!")
            b_success = False

        return b_success

    def add_new_car(self):
        print("┌─────────────────────────────────────────────────┐")
        print("│           • Neues Fahrzeug hinzufügen •         │")
        print("└─────────────────────────────────────────────────┘")

        while True:
            s_id_car = input("▨ Fahrzeug ID festlegen › ")
            if s_id_car == "":
                print("▣ Die Fahrzeug ID muss numerisch sein!")
                continue

            i_id_car = int(s_id_car)

            if i_id_car < 1:
                continue

            # Prüfen ob ID bereits verwendet wird
            b_success, o_car = self.get_car_by_id(i_id_car=i_id_car)
            if b_success is False:
                # Falls nicht:
                break

            print("▣ Die Fahrzeug ID ist bereits vergeben!")

        s_model_code = input("▨ Fahrzeug Modell festlegen › ")
        s_color_code = input("▨ Fahrzeug Farbcode festlegen › ")
        s_extras = input("▨ Fahrzeug Extras festlegen (durch Komma separiert) › ")
        s_right_side = input("▨ R - Rechtslenker | L - Linkslenker › ")
        if s_right_side.upper() == "R":
            i_right_side = 1
        else:
            i_right_side = 0
        s_city_to_ship = input("▨ In welchen Standort soll das Fahrzeug geliefert werden › ")

        # Sanitize SQL replacing apostrophe
        s_model_code = self.replace_apostrophe(s_model_code)
        s_color_code = self.replace_apostrophe(s_color_code)
        s_extras = self.replace_apostrophe(s_extras)
        s_city_to_ship = self.replace_apostrophe(s_city_to_ship)

        o_car = CarDO(i_id_car=i_id_car, s_model_code=s_model_code, s_color_code=s_color_code, s_extras=s_extras, i_right_side=i_right_side, s_city_to_ship=s_city_to_ship)
        b_success = self.insert_car(o_car)

    def see_all_cars(self):
        print("")

        a_o_cars = self.get_all_cars()

        if len(a_o_cars) > 0:
            print(a_o_cars[0].get_car_header_for_list())
        else:
            print("▣ Es befinden sich keine Autos in der Warteschlange!")
            print("")
            return

        for o_car in a_o_cars:
            print(o_car.get_car_info_for_list())

        print("")

    def see_car_by_id(self, i_id_car=0):
        if i_id_car == 0:
            s_id = input("▨ Fahrzeug ID › ")
            i_id_car = int(s_id)

        s_id_car = str(i_id_car)

        b_success, o_car = self.get_car_by_id(i_id_car=i_id_car)
        if b_success is False:
            print("▣ Error, Fahrzeug ID: " + s_id_car + " ist nicht vorhanden.")
            return False

        print("")
        o_car.print_car_info()
        print("")

        return True

    def delete_by_id(self):

        s_id = input("▨ ID von zu löschendem Fahrzeug › :")
        i_id_car = int(s_id)

        if i_id_car == 0:
            print("▣ Error ungültige Id")
            return

        # Wiederverwendung see_car_by_id
        b_found = self.see_car_by_id(i_id_car=i_id_car)
        if b_found is False:
            return

        s_delete = input("▨ Wollen Sie das Fahrzeug wirklich LÖSCHEN. Geben Sie Y zum löschen ein: ")
        if s_delete.upper() == "Y":
            s_sql = "DELETE FROM car_queue WHERE i_id_car=" + str(i_id_car)
            i_num = self.o_mysql.delete(s_sql)

            print("▣ ", i_num, " Zeile(n) gelöscht")

            # if b_success is True:
            #     print("Car deleted successfully from the queue")


if __name__ == "__main__":

    try:

        o_mysql = MySql(s_user="python", s_password="blog.carlesmateo.com-db-password", s_database="carles_database", s_host="127.0.0.1", i_port=3306)

        o_queue_manager = QueueManager(o_mysql=o_mysql)
        o_queue_manager.main_menu()
    except KeyboardInterrupt:
        print("▣ CTRL + C erkannt. Verlassen...")
