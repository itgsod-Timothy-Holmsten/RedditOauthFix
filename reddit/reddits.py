import reddit
from reddit.utils import Utils

url_api = "https://oauth.reddit.com"

url_hot = url_api + "/r/{subreddit}/hot"

class Subreddit():
    def __init__(self, subreddit):
        self.subreddit = subreddit

    def hot(self):
        return reddit.client.request(url_hot.format(subreddit=self.subreddit))

    def hot_children(self):
        return self.hot()['data']['children']

        #return Utils(self.hot()['data']['children'])