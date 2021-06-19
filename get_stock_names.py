import praw
import pandas as pd
import time 


# requires a Reddit account and developer App
username = 'steve55677'
password = 'dickface1'
userAgent = 'wsbscraper' # can be random string
clientId = 'ouT0A38wSJwpaQ'
secretKey = 'CYkJCA_osUfnYxEX8jZKFMaJrCaH5g'
start_time = time.time()


# enter chcp 65001 on cmd prompt to resolve charmap isssues for windows users

# create reddit instance with OAuth2
reddit = praw.Reddit(client_id = clientId, client_secret = secretKey , username=username, password=password, user_agent=userAgent)

subreddit = reddit.subreddit('wallstreetbets')


# join all of this data together and then remove any duplicate values
# rising_topics = subreddit.rising(limit=50)
# trending_topics = subreddit.rising(limit=50)

hot_topics = list(subreddit.hot(limit=500))

potential_stock_names = [] 
trending_stock_names =  []

stock_names_list = pd.read_csv('stock-names-sheet.csv')['Name'].tolist()

for topic in hot_topics:

    headline = topic.title # ex :"Daily Popular Tickers Thread for June 16, 2021 - AMC | CLNE | DKNG"    
    # assuming stock names are 1 - 5 characters long, and all caps
    for i in range(len(headline)):
        try:
            currentCharacterSelection = headline[i:i+5].replace(" ", "")            
            if(currentCharacterSelection.isupper() and currentCharacterSelection.isalnum()):
        
                if currentCharacterSelection in stock_names_list:
                    
                    trending_stock_names.append(currentCharacterSelection)
        except:
            pass

trending_stock_names = list(set(trending_stock_names)) # eliminate duplicates
trending_stocks_rank =  {}

for stock in trending_stock_names:
    trending_stocks_rank[stock] = {'comments': 0, 'upvote_ratio':0, 'score':0}


# ex of trending stocks =   { AMC: {comments: y, upvotes: x } }
# rank trending stock names based on engagement
# we are assuming that the higher a upvote ratio and score
# the higher ranking the stock, or more upside potential for stock gains

for stock in trending_stock_names:
    
    # for loop not being executed
    for post in hot_topics:
        headline = post.title
        # if the stock name is mentioned in the headline, the posts engagement can be used to rank the relevenacy of the stock name in wall street bets 
        
        if stock in headline:
            
            previousScoreCard = trending_stocks_rank[stock]
            new_comments = previousScoreCard['comments'] + len(post.comments)
            new_upvote_ratio = previousScoreCard['upvote_ratio'] + post.upvote_ratio
            new_score = previousScoreCard['score']  + post.score
            
            newScoreCard = {}
        
            newScoreCard['comments']  = new_comments
            newScoreCard['upvote_ratio']  = new_upvote_ratio
            newScoreCard['score']  = new_score

            trending_stocks_rank[stock] = newScoreCard 



for stock in trending_stocks_rank:
    print(stock, trending_stocks_rank[stock])

































print("--- %s seconds ---" % (time.time() - start_time))















