import praw

with open('logs.txt','a+') as logs:
  tokens = config.readlines()
  REDDIT_APP = tokens[4].rstrip()
  REDDIT_USER = tokens[5].rstrip()


def authenticate():
    print('Authenticating...\n')
    reddit = praw.Reddit('ccwbot', user_agent='/u/CCWbot')
    print('Authenticated as {}\n'.format(reddit.user.me()))
    return reddit