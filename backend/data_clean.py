import os
import re
import csv
from collections.abc import Iterator
from bs4 import BeautifulSoup
from scrape import download_episodes, countdown, episodes, path_to_ind

### Data Cleanup
# This file exists to do a bunch of cleanup after a download call.

episodes = 3

this_american_life_episodes = countdown(episodes)
path_to_episode_csv = '/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/transcription-html/'

header = ['episode_id', 'episode title', 'prologue', 'act1 title', 'act1', 'act2 title', 'act2', 'act3 title', 'act3', 'act4 title', 'act4', 'act5 title', 'act5', 'act6 title', 'act6']

def get_episode_title_act_names():

    ## Common html tags that help find the act metadata of an episode
    act1_title_line_before = '<div class="act" id="act1">'
    act2_title_line_before = '<div class="act" id="act2">'
    act3_title_line_before = '<div class="act" id="act3">'
    act4_title_line_before = '<div class="act" id="act4">'
    act5_title_line_before = '<div class="act" id="act5">'
    act6_title_line_before = '<div class="act" id="act6">'
    act7_title_line_before = '<div class="act" id="act7">'
    act8_title_line_before = '<div class="act" id="act8">'
    act9_title_line_before = '<div class="act" id="act9">'

    for episode in this_american_life_episodes:

        path = f'/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/www.thisamericanlife.org/{episode}/transcript.html'

        with open(path) as transcript:

            soup = BeautifulSoup(transcript, 'html.parser')

            soup.title.string
            print(soup.title.string)
            # u'The Dormouse's story'

        with open(path) as transcript:
            lines = transcript.readlines()

            for i in range(0, len(lines)):
                line = lines[i]

                if act1_title_line_before in line:
                    act1_title = lines[i+1]
                    act1_title = act1_title.replace('<h3>', '')
                    act1_title = act1_title.replace('</h3>', '')
                    print(act1_title)

                elif act2_title_line_before in line:
                    act2_title = lines[i+1]
                    act2_title = act2_title.replace('<h3>', '')
                    act2_title = act2_title.replace('</h3>', '')
                    print(act2_title)

                elif act3_title_line_before in line:
                    act3_title = lines[i+1]
                    act3_title = act3_title.replace('<h3>', '')
                    act3_title = act3_title.replace('</h3>', '')
                    print(act3_title)

                elif act4_title_line_before in line:
                    act4_title = lines[i+1]
                    act4_title = act4_title.replace('<h3>', '')
                    act4_title = act4_title.replace('</h3>', '')
                    print(act4_title)

                elif act5_title_line_before in line:
                    act5_title = lines[i+1]
                    act5_title = act5_title.replace('<h3>', '')
                    act5_title = act5_title.replace('</h3>', '')
                    print(act5_title)
                
                elif act6_title_line_before in line:
                    act6_title = lines[i+1]
                    act6_title = act6_title.replace('<h3>', '')
                    act6_title = act6_title.replace('</h3>', '')
                    print(act6_title)

                elif act7_title_line_before in line:
                    act7_title = lines[i+1]
                    act7_title = act7_title.replace('<h3>', '')
                    act7_title = act7_title.replace('</h3>', '')
                    print(act7_title)

                elif act8_title_line_before in line:
                    act8_title = lines[i+1]
                    act8_title = act8_title.replace('<h3>', '')
                    act8_title = act8_title.replace('</h3>', '')
                    print(act8_title)
                
                elif act9_title_line_before in line:
                    act9_title = lines[i+1]
                    act9_title = act9_title.replace('<h3>', '')
                    act9_title = act9_title.replace('</h3>', '')
                    print(act9_title)

get_episode_title_act_names()

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