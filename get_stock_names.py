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


# join all of this data together and then remove any duplicate values
# rising_topics = subreddit.rising(limit=50)
# trending_topics = subreddit.rising(limit=50)

hot_topics = subreddit.hot(limit=50)
trending_stock_names =  []

for topic in hot_topics:

    headline = topic.title # ex :"Daily Popular Tickers Thread for June 16, 2021 - AMC | CLNE | DKNG"
    
    # assuming stock names are exactly 3 in length
    for i in range(len(headline)):

        try:
            currentCharacterSelection = headline[i:i+5].replace(" ", "")
            print(i)
            if(currentCharacterSelection.isupper() and currentCharacterSelection.isalnum()):
                print(currentCharacterSelection)
            # if headline[i:i+2]
        except:
            pass




