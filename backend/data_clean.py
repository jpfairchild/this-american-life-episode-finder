import os
import re
import csv
from collections.abc import Iterator
from bs4 import BeautifulSoup
from scrape import download_episodes, countdown, episodes, path_to_ind

### Data Cleanup
# This file exists to do a bunch of cleanup after a download call.
#TODO Again this needs to be a global variable
episodes = 1

# vars
episode_iterator = countdown(episodes)
path_to_episode_csv = '/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/transcription-html/'

# Method
def organize_data_from_html(episode_iter):
    for episode in episode_iter:
        path = f'/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/www.thisamericanlife.org/{episode}/transcript.html'
        
        # Episode Title
        with open(path) as transcript:

            soup = BeautifulSoup(transcript, 'html.parser')

            soup.title.string
            print('\n')
            print(soup.title.string)
            print('------------------------')
            # 'Int: String'
        
        # Act Title plus full act text
        with open(path) as transcript:

            soup = BeautifulSoup(transcript, 'html.parser')
            act_list = ['prologue', 'act1', 'act2', 'act3', 'act4', 'act5', 'act6', 'act7', 'act8', 'act9']

            for act in act_list:
                if soup.find(attrs={'class':'act', 'id':f'{act}'}) == None:
                    pass
                else:
                    full_act = soup.find(attrs={'class':'act', 'id':f'{act}'})
                    full_act = full_act.get_text(separator=" ")
                    lines = full_act.splitlines()
                    
                    act_title = lines[1]
                    print(lines[1])

                    act_text = lines[3]
                    print(lines[3])

            # Make a loop to do this work
            # check for none, if none, then passs


organize_data_from_html(episode_iterator)


## Move each html file into a new csv of that 
# for episode in this_american_life_episodes:

#     # Check if the episode has been downloaded
#     if os.path.exists(path_to_ind + str(episode)) == True:

#         # open the file in the write mode
#         with open(path_to_episode_csv + str(episode), 'a') as ind:
            
#             # create the csv writer
#             writer = csv.writer(ind)

#             writer.writerow(header)
        

#     else:
#         pass 