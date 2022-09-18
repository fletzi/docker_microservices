from lib.mysqllib import MySql
from do.cardo import CarDO


class QueueManager():

    def __init__(self, o_mysql):
        self.o_mysql = o_mysql

    def exit(self):
        exit(0)

    def main_menu(self):
        while True:
            print("Main Menu")
            print("=========")
            print("")
            print("1. Add new car to queue")
            print("2. List all cars to queue")
            print("3. View car by Id")
            print("4. Delete car from queue by Id")
            print("")
            print("0. Exit")
            print("")

            s_option = input("Choose your option:")
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
            print("Inserted", i_inserted_row_count, " row/s")
            b_success = True
        else:
            print("It was impossible to insert the row")
            b_success = False

        return b_success

    def add_new_car(self):
        print("Add new car")
        print("===========")

        while True:
            s_id_car = input("Enter new ID: ")
            if s_id_car == "":
                print("A numeric Id is needed")
                continue

            i_id_car = int(s_id_car)

            if i_id_car < 1:
                continue

            # Check if that id existed already
            b_success, o_car = self.get_car_by_id(i_id_car=i_id_car)
            if b_success is False:
                # Does not exist
                break

            print("Sorry, this Id already exists")

        s_model_code = input("Enter Model Code:")
        s_color_code = input("Enter Color Code:")
        s_extras = input("Enter extras comma separated:")
        s_right_side = input("Enter R for Right side driven:")
        if s_right_side.upper() == "R":
            i_right_side = 1
        else:
            i_right_side = 0
        s_city_to_ship = input("Enter the city to ship the car:")

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
            print("No cars in queue")
            print("")
            return

        for o_car in a_o_cars:
            print(o_car.get_car_info_for_list())

        print("")

    def see_car_by_id(self, i_id_car=0):
        if i_id_car == 0:
            s_id = input("Car Id:")
            i_id_car = int(s_id)

        s_id_car = str(i_id_car)

        b_success, o_car = self.get_car_by_id(i_id_car=i_id_car)
        if b_success is False:
            print("Error, car id: " + s_id_car + " not located.")
            return False

        print("")
        o_car.print_car_info()
        print("")

        return True

    def delete_by_id(self):

        s_id = input("Enter Id of car to delete:")
        i_id_car = int(s_id)

        if i_id_car == 0:
            print("Invalid Id")
            return

        # reuse see_car_by_id
        b_found = self.see_car_by_id(i_id_car=i_id_car)
        if b_found is False:
            return

        s_delete = input("Are you sure you want to DELETE. Type Y to delete: ")
        if s_delete.upper() == "Y":
            s_sql = "DELETE FROM car_queue WHERE i_id_car=" + str(i_id_car)
            i_num = self.o_mysql.delete(s_sql)

            print(i_num, " Rows deleted")

            # if b_success is True:
            #     print("Car deleted successfully from the queue")


if __name__ == "__main__":

    try:

        o_mysql = MySql(s_user="python", s_password="blog.carlesmateo.com-db-password", s_database="carles_database", s_host="127.0.0.1", i_port=3306)

        o_queue_manager = QueueManager(o_mysql=o_mysql)
        o_queue_manager.main_menu()
    except KeyboardInterrupt:
        print("Detected CTRL + C. Exiting")
