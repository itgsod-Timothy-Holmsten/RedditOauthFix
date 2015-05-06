from reddit import client
from reddit.user import User
from reddit.reddits import Subreddit
from reddit.utils import Utils
from reddit.post import Post, Reply, Comment

tim = client.login('timsbot')
from pprint import pprint
print tim.link_karma()

#tim.submit("timsbot", "self", "A submit", "123 Test")




sub = Subreddit("timsbot")
post = Post("timsbot", "31ggml")

#print post.comments()[1]['data']['children'][1]['data']['replies']['data']['children'][0]

#rep = Reply(post.comments()[1]['data']['children'][1]['data']['replies']['data']['children'][0])

#rep.print_replies(rep)

#print post.comments()[1]['data']['children'][0]

#print post.comments()[1]['data']['children'][1]['data']

com = Reply(post.comments()[1]['data']['children'][1])

print com.print_replies(com)

print "jej"






#for c in range(0, len(k)):
#    print k[c].id()



