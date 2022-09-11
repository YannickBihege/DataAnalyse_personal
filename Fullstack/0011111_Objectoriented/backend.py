import sqlite3


class Database:

    def __init__(self , db): #self convention expected argument
        #create connection
        self.conn = sqlite3.connect("books.db")
        self.cur =self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS  book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year integer , isbn integer)")
        self.conn.commit()

    def insert(self,title,author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author, year, isbn))
        self.conn.commit()
        # self.conn.close()

    def search(self,title ="",author ="", year ="", isbn =""):
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn =?" , (title,author, year, isbn))
        rows = self.cur.fetchall()  #rows is a local variable
        return rows

    def update(self,id,title,author, year, isbn):
        self.cur.execute("UPDATE book SET title=? ,author=? , year =? , isbn =? WHERE id=?",( title,author, year, isbn, id) )
        self.conn.commit()

    def delete(self,id):
        conn = sqlite3.connect("books.db")
        cur =conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?",(id,))
        conn.commit()
        conn.close()


    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def __del__(self): #destroy the object and close the database connection
        self.conn.close()


#connect()
# insert("The lion", "Nick" , "2020", 1)
# insert("Civilization or barbarism", "C. Anta Diop" , "1981", 462)
# insert("The ethiopics", "H. Pratt" , 1978, 129)

#print(search(author="Nick"))
#update(3, "The Ethiopics", "Hugo Pratt" , 1978, 104)
#print(view())

