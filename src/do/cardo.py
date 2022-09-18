
class CarDO():

    def __init__(self, i_id_car=0, s_model_code="", s_color_code="", s_extras="", i_right_side=0, s_city_to_ship=""):
        self.i_id_car = i_id_car
        self.s_model_code = s_model_code
        self.s_color_code = s_color_code
        self.s_extras = s_extras
        self.i_right_side = i_right_side
        self.s_city_to_ship = s_city_to_ship

        # Sizes for render
        self.i_width_id_car = 6
        self.i_width_model_code = 25
        self.i_width_color_code = 25
        self.i_width_extras = 50
        self.i_width_side = 5
        self.i_width_city_to_ship = 15

    def print_car_info(self):
        print("Id:", self.i_id_car)
        print("Model Code:", self.s_model_code)
        print("Color Code:", self.s_color_code)
        print("Extras:", self.s_extras)
        s_side = self.get_word_for_driving_side()
        print("Drive by side:", s_side)
        print("City to ship:", self.s_city_to_ship)

    def get_word_for_driving_side(self):
        if self.i_right_side == 1:
            s_side = "Right"
        else:
            s_side = "Left"

        return s_side

    def get_car_info_for_list(self):

        s_output = str(self.i_id_car).rjust(self.i_width_id_car) + " "
        s_output += self.s_model_code.rjust(self.i_width_model_code) + " "
        s_output += self.s_color_code.rjust(self.i_width_color_code) + " "
        s_output += self.s_extras.rjust(self.i_width_extras) + " "
        s_output += self.get_word_for_driving_side().rjust(self.i_width_side) + " "
        s_output += self.get_s_city_to_ship().rjust(self.i_width_city_to_ship)

        return s_output

    def get_car_header_for_list(self):
        s_output = str("Id Car").rjust(self.i_width_id_car) + " "
        s_output += "Model Code".rjust(self.i_width_model_code) + " "
        s_output += "Color Code".rjust(self.i_width_color_code) + " "
        s_output += "Extras".rjust(self.i_width_extras) + " "
        s_output += "Drive".rjust(self.i_width_side) + " "
        s_output += "City to Ship".rjust(self.i_width_city_to_ship)

        i_total_length = self.i_width_id_car + self.i_width_model_code + self.i_width_color_code + self.i_width_extras + self.i_width_side + self.i_width_city_to_ship
        # Add the space between fields
        i_total_length = i_total_length + 5

        s_output += "\n"
        s_output += "=" * i_total_length

        return s_output

    def get_i_id_car(self):
        return self.i_id_car

    def get_s_model_code(self):
        return self.s_model_code

    def get_s_color_code(self):
        return self.s_color_code

    def get_s_extras(self):
        return self.s_extras

    def get_i_right_side(self):
        return self.i_right_side

    def get_s_city_to_ship(self):
        return self.s_city_to_ship
