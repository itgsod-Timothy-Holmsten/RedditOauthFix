import reddit
from pprint import pprint

url_api = "https://oauth.reddit.com"
url_comments = url_api + "/r/{subreddit}/comments/{article}"

class Post(object):
    def __init__(self, subreddit, id):
        self.id = id
        self.subreddit = subreddit

    def comments(self):
        return reddit.client.request(url_comments.format(subreddit=self.subreddit, article=self.id))

class Comments(object):
    def __init__(self, data):
        self.data = data

    @property
    def comments_with_id(self):
        comments = {}
        comments_length = len(self.data[1]['data']['children'])
        for i in range(0, comments_length):
            pass

class Reply(object):
    def __init__(self, data):
        self.text = data['data']['body']
        self.replies = []

        # Checking if the length of replies is 1 or bigger to see if it contains anything else than just ''
        d = data['data']['replies']
        if len(d) >= 1 and d != None:
            for r in data['data']['replies']['data']['children']:
                self.replies.append(r)

        pprint(self.replies)

    def print_replies(self, reply):
        print reply.text

        for r in reply.replies:
            self.print_replies(Reply(r))

class Comment(object):
    def __init__(self, data):
        self.text = data['data']['body']
        self.replies = []



