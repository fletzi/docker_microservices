import mysql.connector


class MySql:

    def __init__(self, s_user, s_password, s_database, s_host="127.0.0.1", i_port=3306):
        self.s_user = s_user
        self.s_password = s_password
        self.s_database = s_database
        self.s_host = s_host
        self.i_port = i_port

        o_conn = mysql.connector.connect(host=s_host, port=i_port, user=s_user, password=s_password, database=s_database)
        self.o_conn = o_conn

    def query(self, s_query):
        a_rows = []

        o_cursor = self.o_conn.cursor()

        o_cursor.execute(s_query)

        for a_row in o_cursor:
            a_rows.append(a_row)

        o_cursor.close()

        return a_rows

    def insert(self, s_query):

        o_cursor = self.o_conn.cursor()

        o_cursor.execute(s_query)
        i_inserted_row_count = o_cursor.rowcount

        # Make sure data is committed to the database
        self.o_conn.commit()

        return i_inserted_row_count

    def delete(self, s_query):

        o_cursor = self.o_conn.cursor()

        o_cursor.execute(s_query)
        i_deleted_row_count = o_cursor.rowcount

        # Make sure data is committed to the database
        self.o_conn.commit()

        return i_deleted_row_count

    def close(self):

        self.o_conn.close()
