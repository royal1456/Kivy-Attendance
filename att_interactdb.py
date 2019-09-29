import sqlite3 as sql
# everything is instance variable so that all objects have different values
# app.db


class database():
    def __init__(self, lt, nm):
        self.conn = sql.connect(':memory:')
        self.c = self.conn.cursor()
        self.update(lt, nm)
        print(
            f'-----------------connection-created-for-{self.name}.------------------')

    def delete(self, word):
        with self.conn:
            self.c.execute("""delete from """+self.name+""" where date =?""", (word,))

    def update(self, lt, nm):
        with self.conn:
            self.lec_in_day = lt
            self.name = nm

    def create(self):
        with self.conn:
            self.c.execute("""CREATE TABLE IF NOT EXISTS """ + self.name + """ (
                 Day text,
                 Date text Primary key,
                 Lec_a integer,
                 Lec_t integer,
                 Work text not null
                )""")

            self.conn.commit()

    def insert(self, dy, dt, la, lt, w):
        with self.conn:
            self.c.execute("""INSERT INTO """ + self.name + """ VALUES (?,?,?,?,?)""",
                           (dy, dt, la, lt, w))  # tupple pass
            self.conn.commit()

    def show_holidays(self, word):
        with self.conn:
            self.c.execute("""SELECT * FROM """ + self.name +
                           """ where work=? """, (word,))
            com = self.c.fetchall()
        for i in com:
            print(*i)

    def show_all(self):
        with self.conn:
            self.c.execute("""SELECT * FROM """ + self.name)
            com = self.c.fetchall()
            return(com)

    def working_la_lt_find(self):
        with self.conn:
            word = 'w'
            self.c.execute("""SELECT * FROM """ + self.name +
                           """ where work=? """, (word,))
            com = self.c.fetchall()
        self.lt = self.lec_in_day * len(com)
        self.la = 0
        for i in com:
            self.la += i[2]
        return self.la, self.lt

    def percentage(self, *args):  # ________________________bug left readings values
        return(self.la / self.lt * 100)

    #c.execute("""SELECT * FROM DATA where work='w' """)
    # x = c.fetchall()
    # for x in c.fetchall():
    # print(percentage(* working_la_lt_find('data', 'w')))
    # show_holidays('data', 'h')
    def __del__(self):
        print('-----------------connection-deleted.--------------------')
        self.c.close()
