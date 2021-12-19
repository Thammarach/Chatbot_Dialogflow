import sqlite3

# # Building Table name 'Items'
# conn = sqlite3.connect('product.db')
# c = conn.cursor()
# c.execute("""CREATE TABLE items(
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     id_item TEXT,
#                     sum TEXT)""")
#
# Building Table name 'Oder'
# conn = sqlite3.connect('product.db')
# c = conn.cursor()
# c.execute("""CREATE TABLE Oder(
#                      id INTEGER PRIMARY KEY AUTOINCREMENT,
#                      id_user TEXT,
#                      id_item TEXT,
#                      sum TEXT,
#                      datetime DATETIME)""")

# conn = sqlite3.connect('product.db')
# c = conn.cursor()
# c.execute("SELECT * FROM items WHERE id_item == '001' ")
# product = c.fetchall() # keeping selected  Database
#
# print(product[0][2]) # access to index of sum (Database)

conn = sqlite3.connect('product.db')
c = conn.cursor()
c.execute("""SELECT * FROM oder WHERE id_user == 'Uc53a82e111fc8f5c991ebc7ab2313795'""")
product = c.fetchall()
for i in product:
    print(i[2])
