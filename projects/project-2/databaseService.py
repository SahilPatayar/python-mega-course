import sqlite3

class DatabaseService():

    """ 
    A Database Service to handle database operations
    """

    def __init__(self, dbfile):
        self.conn = sqlite3.connect(dbfile)
        self.cur = self.conn.cursor()
        self.createTable()

    def createTable(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS BOOK (ID INTEGER PRIMARY KEY, TITLE TEXT, AUTHOR TEXT, YEAR INTEGER, ISBN INTEGER)")
        self.conn.commit()

    def viewAll(self):
        self.cur.execute("SELECT * FROM BOOK")
        rows = self.cur.fetchall()
        return rows

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO BOOK(ID, TITLE, AUTHOR, YEAR, ISBN) VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE BOOK SET TITLE=?, AUTHOR=?, YEAR=?, ISBN=? WHERE ID=?", (title, author, year, isbn, id))

    def delete(self, id):
        self.cur.execute("DELETE FROM BOOK WHERE ID=?", (id, ))

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM BOOK WHERE TITLE=? or AUTHOR=? or YEAR=? or ISBN=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    pass