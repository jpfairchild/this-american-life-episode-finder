
from bs4 import BeautifulSoup

class fetch_data_from_html():

    # __init__
    # fet = fetch_episode_title(episode_id)
    # fpatat = fetch_prologue_act_titles_act_text(episode_id)
    def __init__(self, id, fet):
        self.id = id
        self.episode_title = fet(self.id)
        self.prologue = None
        self.act1_title = None
        self.act1 = None
        self.act2_title = None
        self.act2 = None
        self.act3_title = None
        self.act3 = None
        self.act4_title = None
        self.act4 = None
        self.act5_title = None
        self.act5 = None
        self.act6_title = None
        self.act6 = None
        self.act7_title = None
        self.act7 = None
        self.act8_title = None
        self.act8 = None
        self.act9_title = None
        self.act9 = None

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


### Fetches ###
# Fetch Title
def fetch_episode_title(episode_id):

    # Pass in the id to get the correct path
    path = f'/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/www.thisamericanlife.org/{episode_id}/transcript.html'

    with open(path) as transcript:
        soup = BeautifulSoup(transcript, 'html.parser')
        if ' - This American Life' in soup.title.string:
            title = soup.title.string
            episode_title = title.replace(' - This American Life', '')
            return episode_title
        else:
            episode_title = soup.title.string
            return episode_title


# Fetch prologue and acts
def fetch_prologue_act_titles_act_text(episode_id):
    path = f'/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/www.thisamericanlife.org/{episode_id}/transcript.html'

    # Act Title plus full act text
    with open(path) as transcript:

        soup = BeautifulSoup(transcript, 'html.parser')
        act_list = ['prologue', 'act1', 'act2', 'act3', 'act4', 'act5', 'act6', 'act7', 'act8', 'act9']

        for act in act_list:

            if soup.find(attrs={'class':'act', 'id':f'{act}'}) == None:
                pass
            else:
                full_act = soup.find(attrs={'class':'act', 'id':f'{act}'})
                full_act = full_act.get_text(separator=' ')
                lines = full_act.splitlines()

                if act == 'prologue':
                    prologue = lines[3].lstrip()
                elif act == 'act1':
                    act1_title = lines[1].lstrip()
                    act1 = lines[3].lstrip()
                elif act == 'act2':
                    act2_title = lines[1].lstrip()
                    act2 = lines[3].lstrip()
                elif act == 'act3':
                    act3_title = lines[1].lstrip()
                    act3 = lines[3].lstrip()
                elif act == 'act4':
                    act4_title = lines[1].lstrip()
                    act4 = lines[3].lstrip()
                elif act == 'act5':
                    act5_title = lines[1].lstrip()
                    act5 = lines[3].lstrip()
                elif act == 'act6':
                    act6_title = lines[1].lstrip()
                    act6 = lines[3].lstrip()
                elif act == 'act7':
                    act7_title = lines[1].lstrip()
                    act7 = lines[3].lstrip()
                elif act == 'act8':
                    act8_title = lines[1].lstrip()
                    act8 = lines[3].lstrip()
                elif act == 'act9':
                    act9_title = lines[1].lstrip()
                    act9 = lines[3].lstrip()


## Test Calls
vr = fetch_data_from_html(451, fetch_episode_title)
# vr.fetch_episode_title()
# vr.fetch_prologue_act_titles_act_text()
print(vr)
