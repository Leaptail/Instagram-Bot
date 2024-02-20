import praw

user_agent = "praw_learn"

class redditlogin:
    def __init__(self, user, passw, id, secret):
        self.user = user
        self.passw = passw
        self.id = id
        self.secret = secret
        
        reddit = praw.Reddit(username = self.user,
                            password = self.passw,
                            client_id = self.id,
                            client_secret = self.secret,
                            user_agent = user_agent)
        
        def scraper(name):
            subreddit = reddit.subreddit(name) 