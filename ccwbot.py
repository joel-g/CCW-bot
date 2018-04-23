import praw
from time import sleep
# 
  

def authenticate():
  print('Authenticating...\n')
  reddit = praw.Reddit('ccwbot', user_agent='/u/CCWbot')
  print('Authenticated as {}\n'.format(reddit.user.me()))
  return reddit

def record_commented(submission_id):
  print("Logging comment...")
  with open("commented.txt", 'a+') as comment_log:
    comment_log.write(submission_id + '\n')

def is_replied(submission_id):
  print("Checking to see if this has already been commented...")
  sleep(1)
  readable = open("logs.txt", "r")
  if submission_id in readable.read().splitlines():
    print("It has been commented.\n")
    sleep(1)
    return True
  else:
    print("It has not been commented.\n")
    sleep(1)
    return False

def get_submissions(reddit):
  print("Fetching new posts...")
  posts = []
  for post in reddit.subreddit('ccw').new(limit=50):
    posts.append(post)
  print("Returning " + str(len(posts)) + " reddit posts")
  return posts

def get_questions(posts):
  print("Pulling questions from list of " + str(len(posts)) + " posts")
  questions = []
  for post in posts:
    if "?" in post.title:
      questions.append(post)
  print("Found " + str(len(questions)) + " questions")
  return questions

def engine(questions):
  for submission in questions:
    if not is_replied(submission.id)
      try:
        submission.reply("It looks like you asked a question in /r/CCW. There's a good chance you're asking what gun you should buy/carry. The answer is a Glock 19.")
        print("Replied to '" + submission.title + "'")
        record_commented(submission.id)
        print("Sleeping 500 seconds")
        sleep(500)
      except:
        "Couldn't reply for some reason"
    sleep


def main():
  reddit = authenticate()
  posts = get_submissions(reddit)
  questions = get_questions(posts)
  engine(questions)

if __name__ == '__main__':
  main()