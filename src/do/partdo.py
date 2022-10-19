
class PartDO():

    def __init__(self, i_id_part=0, s_part_name="", i_part_amount=""):
        self.i_id_part = i_id_part
        self.s_part_name = s_part_name
        self.i_part_amount = i_part_amount

        # Sizes for render
        self.i_width_id_part = 6
        self.i_width_part_name = 25
        self.i_width_part_amount = 5

    def print_part_info(self):
        print("■ Rohstoff ID: ", self.i_id_part)
        print("■ Rohstoff Name: ", self.s_part_name)
        print("■ Menge: ", self.i_part_amount)

    def get_part_info_for_list(self):

        s_output = str(self.i_id_part).rjust(self.i_width_id_part) + " "
        s_output += self.s_part_name.rjust(self.i_width_part_name) + " "
        s_output += str(self.i_part_amount).rjust(self.i_width_part_amount)

        return s_output

    def get_part_header_for_list(self):
        s_output = str("Rohstoff ID").rjust(self.i_width_id_part) + " "
        s_output += "Name".rjust(self.i_width_part_name) + " "
        s_output += "Menge".rjust(self.i_width_part_amount)

        i_total_length = self.i_width_id_part + self.i_width_part_name + self.i_width_part_amount
        # Add the space between fields
        i_total_length = i_total_length + 5

        s_output += "\n"
        s_output += "=" * i_total_length

        return s_output

    def get_i_id_part(self):
        return self.i_id_part

    def get_s_part_name(self):
        return self.s_part_name

    def get_i_part_amount(self):
        return self.i_part_amount
