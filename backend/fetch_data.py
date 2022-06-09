
from bs4 import BeautifulSoup
from scrape import countdown, episodes

class fetch_data_from_html():

    ### __init__
    # fet = fetch_episode_title(episode_id)
    # fat = fetch_act_titles(episode_id)
    # fa = fetch_acts(episode_id)
    def __init__(self, id, fet, fat, fa):
        self.id = id
        self.episode_title = fet(self.id)
        self.prologue = fa(self.id, 'prologue')
        self.act1_title = fat(self.id, 'act1')
        self.act1 = fa(self.id, 'act1')
        self.act2_title = fat(self.id, 'act2')
        self.act2 = fa(self.id, 'act2')
        self.act3_title = fat(self.id, 'act3')
        self.act3 = fa(self.id, 'act3')
        self.act4_title = fat(self.id, 'act4')
        self.act4 = fa(self.id, 'act4')
        self.act5_title = fat(self.id, 'act5')
        self.act5 = fa(self.id, 'act5')
        self.act6_title = fat(self.id, 'act6')
        self.act6 = fa(self.id, 'act6')
        self.act7_title = fat(self.id, 'act7')
        self.act7 = fa(self.id, 'act7')
        self.act8_title = fat(self.id, 'act8')
        self.act8 = fa(self.id, 'act8')
        self.act9_title = fat(self.id, 'act9')
        self.act9 = fa(self.id, 'act9')

    def __repr__(self):
        # attribute_list = [a for a in dir(self) if not a.startswith('__')]
        act_title_list = []
        for attr, value in vars(self).items():
            if value != None:
                for x in ['act1_title', 'act2_title', 'act3_title', 'act4_title', 'act5_title', 'act6_title', 'act7_title', 'act8_title', 'act9_title']:
                    if attr == x:
                        act_title_list.append(value)

        return f' \n id={self.id} \n title={self.episode_title} \n acts={act_title_list} \n'


    # Getters
    def get_episode_id(self):
        return self.id

    def get_episode_title(self):
        return self.episode_title


### ----- Fetches ----- ###
# Fetch Title
def fetch_episode_title(episode_id):

    # Pass in the id to get the correct path
    path = f'/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/www.thisamericanlife.org/{episode_id}/transcript.html'

    with open(path) as transcript:
        soup = BeautifulSoup(transcript, 'html.parser')
        if soup.find('title') == None:
            return None
        elif ' - This American Life' in soup.title.string:
            title = soup.title.string
            title = title.replace(' - This American Life', '')
            episode_title = title.split(' ', 1)[1]
            return episode_title
        else:
            episode_title = soup.title.string
            return episode_title

# There is no episode for 497
# mr = fetch_episode_title(497)
# print(mr)

# d = countdown(episodes)
# for epi in d:
#     vr = fetch_episode_title(epi)
#     print(vr)

# Fetch Act Titles
def fetch_act_titles(episode_id, part):
    path = f'/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/www.thisamericanlife.org/{episode_id}/transcript.html'
    
    # Act title plus full act text
    with open(path) as transcript:

        soup = BeautifulSoup(transcript, 'html.parser')
        # Check if the act exists, most episodes have < 3 acts
        if soup.find(attrs={'class':'act', 'id':f'{part}'}) == None:
            return None
        else:
            full_act = soup.find(attrs={'class':'act', 'id':f'{part}'})
            full_act = full_act.get_text(separator=' ')
            lines = full_act.splitlines()

            # Isolate the title of the act
            act_title = lines[1].strip()
            return act_title

# Fetch Acts Full Text
def fetch_acts(episode_id, part):
    path = f'/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/www.thisamericanlife.org/{episode_id}/transcript.html'
    
    # Act Title plus full act text
    with open(path) as transcript:

        soup = BeautifulSoup(transcript, 'html.parser')

        if soup.find(attrs={'class':'act', 'id':f'{part}'}) == None:
            return None
        else:
            full_act = soup.find(attrs={'class':'act', 'id':f'{part}'})
            full_act = full_act.get_text(separator=' ')
            lines = full_act.splitlines()

            act = lines[3].lstrip()
            return act

## Test Calls
## Testing Act titles, and act text
# ar = fetch_acts(441, 'prologue')
# 421 seems to be werid
# ar = fetch_act_titles(771, 'act2')
# print(ar)

## testing the class
# vr = fetch_data_from_html(454, fetch_episode_title, fetch_act_titles, fetch_acts)
# vr.fetch_episode_title()
# vr.fetch_prologue_act_titles_act_text()
# print(vr)

