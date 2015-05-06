import reddit

url_api = "https://oauth.reddit.com"
url_me = url_api + "/api/v1/me"
url_submit = url_api + "/api/submit"

class User():
    def __init__(self, username):
        self.id = username

    def me(self):
        return reddit.client.request(url_me)

    def link_karma(self):
        return self.me()['link_karma']

    def comment_karma(self):
        return self.me()['comment_karma']

    # Requires atleast 5 karma to submit ( atleast for text [self] )
    def submit(self, subreddit, kind, title, text, link=None):
        if kind == "link" and link:
            data = {'sr': subreddit, 'kind': kind, 'title': title, 'text': text, 'link': link}
        else:
            data = {'sr': subreddit, 'kind': kind, 'title': title, 'text': text}

        return reddit.client.request_with_data(url_submit, data)
