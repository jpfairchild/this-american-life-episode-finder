import os
import re
import csv
from bs4 import BeautifulSoup
from collections.abc import Iterator
from scrape import download_episodes, countdown, episodes, path_to_ind

temp_num = 1

this_american_life_episodes = countdown(temp_num)
path_to_episode_csv = '/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/transcription-html/'
path_to_file = f'/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/www.thisamericanlife.org/{temp_num}/transcript.html'

print(path_to_file)


header = ['episode_id', 'episode title', 'prologue', 'act1 title', 'act1', 'act2 title', 'act2', 'act3 title', 'act3', 'act4 title', 'act4', 'act5 title', 'act5', 'act6 title', 'act6',
          'host1', 'host2', 'host3', 'host4'
         ]


for episode in this_american_life_episodes:

    with open(path_to_file) as transcript:

        soup = BeautifulSoup(transcript, 'html.parser')

        soup.title
        print(soup.title)
        # <title>The Dormouse's story</title>

        soup.title.name
        print(soup.name)
        # u'title'

        soup.title.string
        print(soup.title.string)
        # u'The Dormouse's story'

        soup.title.parent.name
        # u'head'

        soup.p
        # <p class="title"><b>The Dormouse's story</b></p>

        soup.a
        # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

        soup.find_all('a')
        # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
        #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
        #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

        soup.find(id="prologue")
        # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


