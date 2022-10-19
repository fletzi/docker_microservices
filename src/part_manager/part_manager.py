from lib.mysqllib import MySql
from do.cardo import CarDO
#PartDO noch erstellen (do.partdo)


class PartManager():

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
            print("│ [1] Rohstoff zum Lager hinzufügen               │")
            print("│ [2] Lager ausgeben                              │")
            print("│ [3] Rohstoff über ID aus dem Lager entfernen    │")
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

    def get_all_parts(self):
        s_query = "SELECT * FROM part_stock"

        a_rows = self.o_mysql.query(s_query)
        a_o_parts = []

        for a_row in a_rows:
            i_id_part = a_row[0]
            s_part_name = a_row[1]
            i_part_amount = a_row[2]

            o_part = PartDO(i_id_part=i_id_part, s_part_name=s_part_name, i_part_amount=i_part_amount)
            a_o_parts.append(o_part)

        return a_o_cars

    def get_car_by_id(self, i_id_part):
        b_success = False
        o_part = None

        s_query = "SELECT * FROM part_stock WHERE i_id_part=" + str(i_id_part)

        a_rows = self.o_mysql.query(s_query)

        if len(a_rows) == 0:
            # False, None
            return b_success, o_part

        i_id_part = a_rows[0][0]
        s_part_name = a_rows[0][1]
        i_part_amount = a_rows[0][2]

        o_part = PartDO(i_id_part=i_id_part, s_part_name=s_part_name, i_part_amount=i_part_amount)
        b_success = True

        return b_success, o_part

    def replace_apostrophe(self, s_text):
        return s_text.replace("'", "´")

    def insert_part(self, o_car):

        s_sql = """INSERT INTO part_stock 
                                (i_id_part, s_part_name, i_part_amount) 
                         VALUES 
                                (""" + str(o_part.get_i_id_part()) + ", '" + o_part.get_s_part_name() + "', '" + o_part.get_i_part_amount() + "');"

        i_inserted_row_count = self.o_mysql.insert(s_sql)

        if i_inserted_row_count > 0:
            print("■ ", i_inserted_row_count, " Zeile(n) eingefügt")
            b_success = True
        else:
            print("▣ Einfügen der Zeile ist Fehlgeschlagen!")
            b_success = False

        return b_success

    def add_new_part(self):
        print("┌─────────────────────────────────────────────────┐")
        print("│           • Neuen Rohstoff hinzufügen •         │")
        print("└─────────────────────────────────────────────────┘")

        while True:
            s_id_part = input("▨ Rohstoff ID festlegen › ")
            if s_id_part == "":
                print("▣ Die Rohstoff ID muss numerisch sein!")
                continue

            i_id_part = int(s_id_part)

            if i_id_part < 1:
                continue

            # Prüfen ob ID bereits verwendet wird
            b_success, o_part = self.get_part_by_id(i_id_part=i_id_part)
            if b_success is False:
                # Falls nicht:
                break

            print("▣ Die Rohstoff ID ist bereits vergeben!")

        s_part_name = input("▨ Rohstoff Name festlegen › ")
        i_part_amount = input("▨ Rohstoff Menge festlegen › ")

        # Sanitize SQL replacing apostrophe
        s_part_name = self.replace_apostrophe(s_part_name)
        i_part_amount = self.replace_apostrophe(i_part_amount)

        o_part = PartDO(i_id_part=i_id_part, s_part_name=s_part_name, i_part_amount=i_part_amount)
        b_success = self.insert_car(o_car)

    def see_all_parts(self):
        print("")

        a_o_parts = self.get_all_parts()

        if len(a_o_parts) > 0:
            print(a_o_parts[0].get_part_header_for_list())
        else:
            print("▣ Es befinden sich keine Rohstoffe im Lager!")
            print("")
            return

        for o_part in a_o_parts:
            print(o_part.get_part_info_for_list())

        print("")

    def see_part_by_id(self, i_id_part=0):
        if i_id_part == 0:
            s_id = input("▨ Rohstoff ID › ")
            i_id_part = int(s_id)

        s_id_part = str(i_id_part)

        b_success, o_part = self.get_part_by_id(i_id_part=i_id_part)
        if b_success is False:
            print("▣ Error, Rohstoff ID: " + s_id_part + " ist nicht vorhanden.")
            return False

        print("")
        o_part.print_part_info()
        print("")

        return True

    def delete_by_id(self):

        s_id = input("▨ ID von zu löschendem Rohstoff › :")
        i_id_part = int(s_id)

        if i_id_part == 0:
            print("▣ Error ungültige Id")
            return

        # Wiederverwendung see_car_by_id
        b_found = self.see_part_by_id(i_id_part=i_id_part)
        if b_found is False:
            return

        s_delete = input("▨ Wollen Sie den Rohstoff wirklich LÖSCHEN. Geben Sie Y zum löschen ein: ")
        if s_delete.upper() == "Y":
            s_sql = "DELETE FROM part_stock WHERE i_id_part=" + str(i_id_part)
            i_num = self.o_mysql.delete(s_sql)

            print("▣ ", i_num, " Zeile(n) gelöscht")

if __name__ == "__main__":

    try:

        o_mysql = MySql(s_user="python", s_password="blog.carlesmateo.com-db-password", s_database="carles_database", s_host="127.0.0.1", i_port=3306)

        o_part_manager = PartManager(o_mysql=o_mysql)
        o_part_manager.main_menu()
    except KeyboardInterrupt:
        print("▣ CTRL + C erkannt. Verlassen...")
