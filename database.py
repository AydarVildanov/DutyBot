import datetime
import sqlite3


class DateTime:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('date.db')
            self.cursor = self.conn.cursor()

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
        flag = False
        day_ = int(datetime.datetime.today().day)
        month_ = int(datetime.datetime.today().month)
        year_ = int(datetime.datetime.today().year)

        if day_ != self.day or month_ != self.month or year_ != self.year:
            try:
                flag = True
                self.cursor.execute("UPDATE DATE SET day == ? WHERE id == 0", (day_,))
                self.cursor.execute("UPDATE DATE SET month = ? WHERE id == 0", (month_,))
                self.cursor.execute("UPDATE DATE SET year = ? WHERE id == 0", (year_,))
                self.cursor.execute("UPDATE DATE SET counter = ? WHERE id == 0", (self.counter + 1,))
                self.conn.commit()

                self.cursor.close()

                print("Данные успешно обновлены")
            except sqlite3.Error as error:
                print("Ошибка при подключении к sqlite", error)
        if flag:
            return self.counter + 1
        else:
            return self.counter
