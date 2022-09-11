import sqlite3



def create_table():
    conn = sqlite3.connect("lite.db")
    cur =conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS  store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item,quantity, price):
    conn = sqlite3.connect("lite.db")
    cur =conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()




def view():
    conn = sqlite3.connect("lite.db")
    cur =conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur =conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = sqlite3.connect("lite.db")
    cur =conn.cursor()
    cur.execute("UPDATE store SET quantity=? ,price=? WHERE item =?",(quantity,price,item))
    conn.commit()
    conn.close()


#create_table()
# insert("Coffe Cup", 10, 5)
delete('Coffe Cup')
delete("Vimto ")
delete('Ginger Beer')
delete('Wine glass')

# insert("Wine glass", 10, 5)
# insert("Ginger Beer", 10, 5)
# insert("Vimto ", 10, 5)
#update("Ginger Beer", 200, 15)
print(view())