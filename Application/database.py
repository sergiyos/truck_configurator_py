import mysql.connector
from mysql.connector import errorcode


class DataBase:

    __user = "root"
    __password = "5123"
    __host = "localhost"
    __database = "truck"

    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user=self.__user, password=self.__password,
                                          host=self.__host, database=self.__database)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Невірний пароль або логін!")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("База даних не існує!")
            else:
                print(err)
        self.cursor = self.cnx.cursor()

    def select_data(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cnx.close()












