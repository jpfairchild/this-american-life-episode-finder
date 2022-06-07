
import sqlite3

conn = sqlite3.connect(':memory:')
# conn = sqlite3.connect('tal_transcripts.db')

c = conn.cursor()

c.execute("""CREATE TABLE episodes (
            id integer,
            episode_title text,
            prologue text,
            act1_title text,
            act1 text,
            act2_title text,
            act2 text,
            act3_title text,
            act3 text,
            act4_title text,
            act4 text,
            act5_title text,
            act5 text,
            act6_title text,
            act6 text,
            act7_title text,
            act7 text,
            act8_title text,
            act8 text,
            act9_title text,
            act9 text
            )""")

conn.commit()

conn.close()