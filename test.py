import praw


# requires a Reddit account and developer App
username = 'steve55677'
password = 'dickface1'
userAgent = 'wsbscraper' # can be random string
clientId = 'ouT0A38wSJwpaQ'
secretKey = 'CYkJCA_osUfnYxEX8jZKFMaJrCaH5g'














# enter chcp 65001 on cmd prompt to resolve charmap isssues for windows users

# create reddit instance with OAuth2
reddit = praw.Reddit(client_id = clientId, client_secret = secretKey , username=username, password=password, user_agent=userAgent)


subreddit = reddit.subreddit('wallstreetbets')

rising_topics = subreddit.rising(limit=50)
trending_topics = subreddit.rising(limit=50)

hot_topics = subreddit.hot(limit=10)

i= 0
for topic in hot_topics:
    print(i)
    print(topic.title)
    print(topic.id)
    print(topic.author)
    print(topic.created_utc)
    print(topic.score)
    print(topic.upvote_ratio)
    print(topic.url)


    i+=1


# hot_topics = subreddit.hot(limit=50)
# i= 0
# for topic in hot_topics:
    
#     if not topic.stickied:
#         print(i ,topic.title)
#     i+=1
    










