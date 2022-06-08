
import sqlite3
from fetch_data import fetch_data_from_html


conn = sqlite3.connect(':memory:')
# conn = sqlite3.connect('tal_transcripts.db')

# conn.create_function('populate', 1, fetch_data_from_html)

c = conn.cursor()

# c.execute("""CREATE TABLE num (
#             id INTEGER,
#             )""")

c.execute("""CREATE TABLE IF NOT EXISTS episodes (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            episode_title TEXT NOT NULL,
            prologue TEXT NONE,
            act1_title TEXT NONE,
            act1 TEXT NONE,
            act2_title TEXT NONE,
            act2 TEXT NONE,
            act3_title TEXT NONE,
            act3 TEXT NONE,
            act4_title TEXT NONE,
            act4 TEXT NONE,
            act5_title TEXT NONE,
            act5 TEXT NONE,
            act6_title TEXT NONE,
            act6 TEXT NONE,
            act7_title TEXT NONE,
            act7 TEXT NONE,
            act8_title TEXT NONE,
            act8 TEXT NONE,
            act9_title TEXT NONE,
            act9 TEXT NONE
            )""")

### Data insert

ep_451 = fetch_data_from_html(451)

# c.execute("INSERT INTO episodes VALUES (1, 'Test Title', 'Test Prologue Text', Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null)")
# c.execute("INSERT INTO episodes VALUES (2, 'Test Title 2', 'Test Prologue Text', Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null)")


c.execute("SELECT * FROM episodes WHERE prologue='Test Prologue Text'")

print(c.fetchall())

conn.commit()
conn.close()




# try:
#     sqliteConnection = sqlite3.connect('SQLite_Python.db')
#     cursor = sqliteConnection.cursor()
#     print("Successfully Connected to SQLite")

#     # sqlite_insert_query = """INSERT INTO SqliteDb_developers
#     #                       (id, name, email, joining_date, salary) 
#     #                        VALUES 
#     #                       (1,'James','james@pynative.com','2019-03-17',8000)"""

#     # count = cursor.execute(sqlite_insert_query)
#     # sqliteConnection.commit()
#     # print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
#     # cursor.close()

# except sqlite3.Error as error:
#     print("Failed to insert data into sqlite table", error)
    
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("The SQLite connection is closed")