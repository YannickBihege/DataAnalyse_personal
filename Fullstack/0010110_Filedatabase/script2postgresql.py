import psycopg2




def create_table():
    conn = psycopg2.connect("dbname ='postgres'  user='postgres'  password ='xboxer89'  host='localhost' port= '5432' ")
    cur =conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS  store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity, price):
    conn = psycopg2.connect("dbname ='postgres'  user='postgres'  password ='xboxer89'  host='localhost' port= '5432' ")
    cur =conn.cursor()
    #cur.execute("INSERT INTO store VALUES('%s','%s','%s')" %(item,quantity,price)) #sql injection
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)" ,(item,quantity,price)) #safer ?
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname ='postgres'  user='postgres'  password ='xboxer89'  host='localhost' port= '5432' ")

    cur =conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname ='postgres'  user='postgres'  password ='xboxer89'  host='localhost' port= '5432' ")

    cur =conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = psycopg2.connect("dbname ='postgres'  user='postgres'  password ='xboxer89'  host='localhost' port= '5432' ")
    cur =conn.cursor()
    cur.execute("UPDATE store SET quantity=%s ,price=%s WHERE item =%s",(quantity,price,item))
    conn.commit()
    conn.close()


create_table()
#insert("Coffe Cup", 10, 5)
#delete('Coffe Cup')
# delete("Vimto ")
# delete('Ginger Beer')
# delete('Wine glass')

# insert("Wine glass", 10, 5)
# insert("Ginger Beer", 10, 5)
# insert("Vimto ", 10, 5)
update( 200, 15 ,"Ginger Beer")
print(view())