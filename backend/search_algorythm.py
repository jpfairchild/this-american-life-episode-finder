import sqlite3
import os
import sys

search_keywords = ['Poultry Slam 1995', 'Anger and Forgiveness', '500!']


try:
    ### Connect to DB
    # conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect('tal_transcripts.db')

    c = conn.cursor()
    select_acts = conn.cursor()
    print("Successfully Connected to DB")



    ### Start of Functions
    # vars
    count = 0

    # Create and return a [{'episode_title': 'episode_title', 'act_title':, 13, 'word': 3, 'word': 3, 'word': 3, 'word': 2}, {}, {}...]
    def find_amount_in_transcript(search):
        data_lookup = []
        act_hits = []
        i = 0

        for key in search:
            print(key)
            # c.execute("SELECT id, episode_title FROM episodes WHERE id=:id", {'id': 497})
            c.execute("SELECT id, episode_title, act1_title, act2_title FROM episodes WHERE episode_title=:episode_title", {'episode_title': key})
            # print(c.fetchall)
            n = c.fetchone()
            if n == None:
                pass
            else:
                ln = list(n)
                act_hits.append(ln)

        return act_hits
        
        
    # print(c.fetchall())
        # for row in c:
        #     print(select_acts.fetchall())

    # for item in :
    #     if item not in counted_items:
    #         print(item)
    #         counted_items[item] = 1
    #     else:
    #         counted_items[item] += 1

    # opening_count = Counter(opening)
    # print(opening_count)
    # closing_count = Counter(closing)
    # opening_count.subtract(closing_count) # Quickly and effiantly get the sold products from two inventorys
    # return opening_count[item]


    def search_lookup():

        first_result, second_result, third_result = find_amount_in_transcript(search_keywords)
        print(search_keywords)


    
    ### Call Functions
    # find_amount_in_transcript()
    key1_results = find_amount_in_transcript(search_keywords)
    print(key1_results)

    # print("Record inserted successfully into SqliteDb_developers table ", c.rowcount)
    c.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
    
finally:
    if conn:
        conn.close()
        print("The SQLite connection is closed")