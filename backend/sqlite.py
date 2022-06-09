
import sqlite3
import os
from fetch_data import fetch_data_from_html
from fetch_data import fetch_episode_title, fetch_act_titles, fetch_acts
from scrape import countdown, episodes, path_to_ind


try:
    ### Connect to DB
    # conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect('tal_transcripts.db')

    c = conn.cursor()
    print("Successfully Connected to DB")

    c.execute("""CREATE TABLE IF NOT EXISTS episodes (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                episode_title TEXT NONE,
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


    ### ------ Pass Data Functions ------ ###
    # Pass All data
    def pass_all_data():
        # Fetch all episodes using a generator
        this_american_life_episodes = countdown(episodes)

        for episode in this_american_life_episodes:

                # if the transcript exists, then pass it to the database
                if os.path.exists(path_to_ind + str(episode)) == True:

                    ### Data insert
                    epi  = fetch_data_from_html(episode, fetch_episode_title, fetch_act_titles, fetch_acts)
                    # Inserting using class call
                    c.execute("""INSERT INTO episodes VALUES (:id, 
                                                            :episode_title, 
                                                            :prologue, 
                                                            :act1_title, 
                                                            :act1, 
                                                            :act2_title, 
                                                            :act2, 
                                                            :act3_title, 
                                                            :act3, 
                                                            :act4_title, 
                                                            :act4, 
                                                            :act5_title, 
                                                            :act5, 
                                                            :act6_title, 
                                                            :act6, 
                                                            :act7_title, 
                                                            :act7, 
                                                            :act8_title, 
                                                            :act8, 
                                                            :act9_title, 
                                                            :act9)""",
                                                            {"id": epi.id,
                                                            "episode_title": epi.episode_title, 
                                                            "prologue": epi.prologue, 
                                                            "act1_title": epi.act1_title, 
                                                            "act1": epi.act1, 
                                                            "act2_title": epi.act2_title, 
                                                            "act2": epi.act2, 
                                                            "act3_title": epi.act3_title, 
                                                            "act3": epi.act3, 
                                                            "act4_title": epi.act4_title, 
                                                            "act4": epi.act4, 
                                                            "act5_title": epi.act5_title, 
                                                            "act5": epi.act5, 
                                                            "act6_title": epi.act6_title, 
                                                            "act6": epi.act6, 
                                                            "act7_title": epi.act7_title, 
                                                            "act7": epi.act7, 
                                                            "act8_title": epi.act8_title, 
                                                            "act8": epi.act8, 
                                                            "act9_title": epi.act9_title, 
                                                            "act9": epi.act9})
                    print(str(episode) + ' has been uploaded to the database successfully')            
                else:
                    print('fuck')

    # Pass a single episode
    #TODO Set this to run once a week, checking if a new episode as been released
    def pass_single_episode(episode):

        # if the transcript exists, then pass it to the database
        if os.path.exists(path_to_ind + str(episode)) == True:

            ### Data insert
            epi  = fetch_data_from_html(episode, fetch_episode_title, fetch_act_titles, fetch_acts)
            # Inserting using class call
            c.execute("""INSERT INTO episodes VALUES (:id, 
                                                    :episode_title, 
                                                    :prologue, 
                                                    :act1_title, 
                                                    :act1, 
                                                    :act2_title, 
                                                    :act2, 
                                                    :act3_title, 
                                                    :act3, 
                                                    :act4_title, 
                                                    :act4, 
                                                    :act5_title, 
                                                    :act5, 
                                                    :act6_title, 
                                                    :act6, 
                                                    :act7_title, 
                                                    :act7, 
                                                    :act8_title, 
                                                    :act8, 
                                                    :act9_title, 
                                                    :act9)""",
                                                    {"id": epi.id,
                                                    "episode_title": epi.episode_title, 
                                                    "prologue": epi.prologue, 
                                                    "act1_title": epi.act1_title, 
                                                    "act1": epi.act1, 
                                                    "act2_title": epi.act2_title, 
                                                    "act2": epi.act2, 
                                                    "act3_title": epi.act3_title, 
                                                    "act3": epi.act3, 
                                                    "act4_title": epi.act4_title, 
                                                    "act4": epi.act4, 
                                                    "act5_title": epi.act5_title, 
                                                    "act5": epi.act5, 
                                                    "act6_title": epi.act6_title, 
                                                    "act6": epi.act6, 
                                                    "act7_title": epi.act7_title, 
                                                    "act7": epi.act7, 
                                                    "act8_title": epi.act8_title, 
                                                    "act8": epi.act8, 
                                                    "act9_title": epi.act9_title, 
                                                    "act9": epi.act9})
            print(str(episode) + ' has been uploaded to the database successfully')            
        else:
            print('fuck')

    ### Pass Function Calls
    # pass_all_data()
    # pass_single_episode(500)

    #count = c.execute(sqlite_insert_query)
    c.execute("SELECT * FROM episodes WHERE episode_title=:episode_title", {'episode_title': None})

    # print(c.fetchone())
    # print(c.fetchmany(2))
    print(c.fetchall())

    conn.commit()
    # print("Record inserted successfully into SqliteDb_developers table ", c.rowcount)
    c.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
    
finally:
    if conn:
        conn.close()
        print("The SQLite connection is closed")