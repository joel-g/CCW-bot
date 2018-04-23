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
  with open('logs.txt','a+') as logs:
    for submission in questions:
      if submission.id not in logs:
        try:
          submission.reply("It looks like you asked a question in /r/CCW. There's a good chance you're asking what gun you should buy/carry. The answer is a Glock 19.")
          print("Replied to '" + submission.title + "'")
          logs.write(str(submission.id) + "\n")
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