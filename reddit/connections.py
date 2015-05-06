import getpass
import keyring
import requests
from pprint import pprint
import sys

from reddit import config
from reddit.user import User

app_name = config['app_name']

token_url = "https://www.reddit.com/api/v1/access_token"


class Client():

    def __init__(self):

        self.client_id = keyring.get_password(app_name,'client_id')
        self.client_secret = keyring.get_password(app_name,'client_secret')

        if not (self.client_id or self.client_secret):
                self.client_id = getpass.getpass("Your reddit bot client id: ")
                self.client_secret = getpass.getpass("Your reddit bot client secret: ")

                # save it for next time
                keyring.set_password(app_name,'client_id',self.client_id)
                keyring.set_password(app_name,'client_secret',self.client_secret)


    def login(self, reddit_id):

        passwd = keyring.get_password(app_name, reddit_id)

        if not passwd:
            passwd = getpass.getpass()

            # save it for next time
            keyring.set_password(app_name, reddit_id, passwd)


        headers = {"User-Agent": config['reddit_boot']}



        auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
        data = {'grant_type': 'password' ,'username': reddit_id, 'password': passwd}

        response = requests.post(token_url,data=data,auth=auth,headers=headers)

        if response.status_code != 200:
            pprint(response.json())
            sys.exit()

        json_data= response.json()

        self.access_token = json_data['access_token']

        return User(reddit_id)

    def request(self,uri):

        headers = {"User-Agent": config['reddit_boot']}
        headers['Authorization'] = 'bearer %s' % self.access_token

        response = requests.get(uri,headers=headers)


        print response.headers

        return response.json()