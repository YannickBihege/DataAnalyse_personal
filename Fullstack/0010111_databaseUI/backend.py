import sqlite3

def connect():
    #create connection
    conn = sqlite3.connect("books.db")
    #set a cursor
    cur =conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS  book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year integer , isbn integer)")
    conn.commit()
    conn.close()


def insert(title,author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur =conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author, year, isbn))
    conn.commit()
    conn.close()

def search(title ="",author ="", year ="", isbn =""):
    conn = sqlite3.connect("books.db")
    cur =conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn =?" , (title,author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def update(id,title,author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur =conn.cursor()  #follow the order of the string
    cur.execute("UPDATE book SET title=? ,author=? , year =? , isbn =? WHERE id=?",( title,author, year, isbn, id) )
    conn.commit()
    conn.close()



def delete(id):
    conn = sqlite3.connect("books.db")
    cur =conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()



def view():
    conn = sqlite3.connect("books.db")
    cur =conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

connect()
# insert("The lion", "Nick" , "2020", 1)
# insert("Civilization or barbarism", "C. Anta Diop" , "1981", 462)
# insert("The ethiopics", "H. Pratt" , 1978, 129)

#print(search(author="Nick"))
update(3, "The Ethiopics", "Hugo Pratt" , 1978, 104)
print(view())