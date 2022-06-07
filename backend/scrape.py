
import os
import shutil
from pywebcopy import save_webpage

### Check if the path exists
# paths
path_to_raw_data = '/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/www.thisamericanlife.org'
path_to_html = '/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/transcription-html'
path_to_ind = '/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/www.thisamericanlife.org/'
not_essential_site_data = ['/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/hw1.thisamericanlife.org',
                            '/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/hw2.thisamericanlife.org',
                            '/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/hw3.thisamericanlife.org',
                            '/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/hw4.thisamericanlife.org',
                            '/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data/tal-site-data/use.typekit.net'
                          ]
# Total episodes
# TODO: Make this episode counter dynamic to number of episodes online. Right now hardcoded.
episodes = 771

def countdown(count):
    while count > 0:
        count_left = yield count
        if count_left != None:
            count = count_left
        else:
            count -= 1

# countdown_generator = (episode for episode in range(episodes, -1,-1))

this_american_life_episodes = countdown(episodes)

def download_episodes():

    for episode in this_american_life_episodes:

        # if the transcript exists, don't try downloading it
        if os.path.exists(path_to_ind + str(episode)) == True:
            pass
        
        #TODO Impliment a check to see if the url exists, have this be the way we check if new episodes are posted
        elif episode > 0:
            save_webpage(
                url=f"https://www.thisamericanlife.org/{episode}/transcript",
                project_folder="/Users/dangercat/Documents/GitHub/this-american-life-episode-finder/data",
                project_name="tal-site-data",
                bypass_robots=True,
                debug=False,
                open_in_browser=False,
                delay=None,
                threaded=False,
            )

        elif episode == 0:
            this_american_life_episodes.close()
    
    ## Gets rid of non_essential_data collected in the download process
    for path in not_essential_site_data:
        if os.path.exists(path) == False:
            pass
        elif os.path.exists(path) == True:
            shutil.rmtree(path)


download_episodes()

