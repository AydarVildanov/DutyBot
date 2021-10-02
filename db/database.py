import datetime
import sqlite3


class DateTime(object):
    def __init__(self):
        try:
            sqlite_connection = sqlite3.connect('date.db')
            self.cursor = sqlite_connection.cursor()

            # принимаю аргументы
            sql = "SELECT * FROM DATE"
            self.cursor.execute(sql)

            self.day = self.cursor.fetchall()[0][0]
            # месяц
            self.cursor.execute(sql)

            self.month = self.cursor.fetchall()[0][1]
            # год
            self.cursor.execute(sql)

            self.year = self.cursor.fetchall()[0][2]
            # счетчик
            self.cursor.execute(sql)

            self.counter = self.cursor.fetchall()[0][3]

            print("База данных успешно подключена к SQLite")
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)

    def function_for_correct_date(self):
        day_ = int(datetime.datetime.today().day)
        month_ = int(datetime.datetime.today().month)
        year_ = int(datetime.datetime.today().year)

        if day_ != self.day or month_ != self.month or year_ != self.year:
            try:
                print("ok")
                self.cursor.execute("UPDATE DATE SET day = ? WHERE id = '0'", (day_, ))
                self.cursor.execute("UPDATE DATE SET month = ?", (month_, ))
                self.cursor.execute("UPDATE DATE SET year = ?", (year_, ))
                self.cursor.execute("UPDATE DATE SET counter = ?", (self.counter + 1, ))

                self.cursor.close()

                print("Данные успешно обновлены")
                return self.day, self.month, self.year, self.counter
            except sqlite3.Error as error:
                print("Ошибка при подключении к sqlite", error)


a = DateTime()
d, m, y, c = a.function_for_correct_date()
print(d, m, y, c)
