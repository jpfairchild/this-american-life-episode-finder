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

# Two iterators, one to get titles, and the other for getting full act transcripts
title_iterator = countdown(episodes)
act_iterator = countdown(episodes)
path_to_episode_csv = '/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/transcription-html/'

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

def get_episode_title_act_names():

    for episode in title_iterator:

        path = f'/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/www.thisamericanlife.org/{episode}/transcript.html'

        with open(path) as transcript:

            soup = BeautifulSoup(transcript, 'html.parser')

            soup.title.string
            print(soup.title.string)
            print('--------------------------------')
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
                
                
            print('\n')



def get_act_transcripts():
    for episode in act_iterator:
        path = f'/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/www.thisamericanlife.org/{episode}/transcript.html'

        with open(path) as transcript:
            soup = BeautifulSoup(transcript, 'html.parser')

            while act is not None:

            # Make a loop to do this work
            # check for none, if none, then pass

            # Prologue
            prologue = soup.find(attrs={'class':'act', 'id':'prologue'})
            prologue = prologue.get_text(separator=" ")
            print(prologue)
            # Act 1
            act1 = soup.find(attrs={'class':'act', 'id':f'{act}'})
            act1 = act1.get_text(separator=" ")
            print(act1)
            # Act 2
            act2 = soup.find(attrs={'class':'act', 'id':'act2'})
            act2 = act2.get_text(separator=" ")
            print(act2)
            # Act 3
            act3 = soup.find(attrs={'class':'act', 'id':'act3'})
            act3 = act3.get_text(separator=" ")
            print(act3)
            # Act 4
            act4 = soup.find(attrs={'class':'act', 'id':'act4'})
            act4 = act4.get_text(separator=" ")
            print(act4)
            # Act 5
            act5 = soup.find(attrs={'class':'act', 'id':'act5'})
            act5 = act5.get_text(separator=" ")
            print(act5)
            # Act 6
            act6 = soup.find(attrs={'class':'act', 'id':'act6'})
            act6 = act6.get_text(separator=" ")
            print(act6)
            # Act 7
            act7 = soup.find(attrs={'class':'act', 'id':'act7'})
            act7 = act7.get_text(separator=" ")
            print(act7)
            # Act 8
            act8 = soup.find(attrs={'class':'act', 'id':'act8'})
            act8 = act8.get_text(separator=" ")
            print(act8)
            # Act 9
            act9 = soup.find(attrs={'class':'act', 'id':'act9'})
            act9 = act9.get_text(separator=" ")
            print(act9)




get_act_transcripts()

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