import keyring
import requests
import sys
import pprint

from reddit.user import User

token_url = "https://www.reddit.com/api/v1/access_token"

class Client():
    def __init__(self):

        # Get client id and client secret for our client
        self.client_id = keyring.get_password("redditbot", "client_id")
        self.client_secret = keyring.get_password("redditbot", "client_secret")

        # If client id or client secret is 'null' then ask the user for a client id and secret
        if not (self.client_id or self.client_secret):
            client_id = raw_input("Please type your reddit client id: ")
            client_secret = raw_input("Please type your client secret: ")

            # Save client id and secret
            self.client_id = keyring.set_password("redditbot", "client_id", client_id)
            self.client_secret = keyring.set_password("redditbot", "client_secret", client_secret)

    def login(self, username):
        password = keyring.get_password("redditbot", username)

        if not password:
            password = raw_input("Please type your password: ")

            keyring.set_password("redditbot", username, password)

        # <platform>:<app ID>:<version string> (by /u/<reddit username>)
        headers = {'User-Agent': 'Python: timsbot: v0.1 (by /u/timsbot)'}

        auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
        data = {'grant_type': 'password', 'username': username, 'password': password}

        # Make an authentication post to get the access token
        response = requests.post(token_url, data=data, auth=auth, headers=headers)

        # If the response did not go through
        if response.status_code != 200:
            pprint(response.json)
            sys.exit()

        json_data = response.json()

        self.access_token = json_data['access_token']

        return User(username)

    def request(self, uri):

        headers = {'User-Agent': 'Python: timsbot: v0.1 (by /u/timsbot)'}
        headers['Authorization'] = 'bearer %s' %self.access_token

        response = requests.get(uri, headers=headers)

        return response.json()

    def request_with_data(self, uri, data, method="post"):

        headers = {'User-Agent': 'Python: timsbot: v0.1 (by /u/timsbot)'}
        headers['Authorization'] = 'bearer %s' %self.access_token

        if method == "post":
            response = requests.post(uri, data=data, headers=headers)
        else:
            response = requests.get(uri, data=data, headers=headers)

        return response.json()










