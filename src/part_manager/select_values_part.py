import mysql.connector

if __name__ == "__main__":
    o_conn = mysql.connector.connect(user='python', password='blog.carlesmateo.com-db-password', database='carles_database')
    o_cursor = o_conn.cursor()

    s_query = "SELECT * FROM part_stock"

    o_cursor.execute(s_query)

    for a_row in o_cursor:
        print(a_row)

    o_cursor.close()
    o_conn.close()