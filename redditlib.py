import praw
import pandas as pd

user_agent = "praw_learn"

class redditlogin:
    def __init__(self, user, passw, id, secret):
        self.user = user
        self.passw = passw
        self.id = id
        self.secret = secret
        
        
        
    def scraper(self, name):
        titles = []
        scores = []
        ids = []

        reddit = praw.Reddit(username = self.user,
                            password = self.passw,
                            client_id = self.id,
                            client_secret = self.secret,
                            user_agent = user_agent)
        
        df = pd.DataFrame()

        subreddit = reddit.subreddit(name) 

        for submission in subreddit.new(limit=10):
            titles.append(submission.title)
            scores.append(submission.score) #upvotes
            ids.append(submission.id)

        df['Title'] = titles
        df['Id'] = ids
        df['Upvotes'] = scores

        print(df.shape)
        df.head(10)
