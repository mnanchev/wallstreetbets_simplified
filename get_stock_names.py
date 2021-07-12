import praw
import pandas as pd
import time 
import requests
import json


# requires a Reddit account and developer App
username = 'steve55677'
# r'C:\Users\walee\Desktop\redditpass.txt'

# f = open('C:\Users\walee\Desktop\redditpass.txt', "r").readline()
# print(f.readline())


password = open('C:\\Users\\walee\\Desktop\\redditpass.txt', "r").read()

userAgent = 'wsbscraper' # can be random string
clientId = 'ouT0A38wSJwpaQ'
secretKey = 'CYkJCA_osUfnYxEX8jZKFMaJrCaH5g'
start_time = time.time()


# enter chcp 65001 on cmd prompt to resolve charmap isssues for windows users




def getData():
    # gets information from r/wallstreetbets

    # create reddit instance with OAuth2
    reddit = praw.Reddit(client_id = clientId, client_secret = secretKey , username=username, password=password, user_agent=userAgent)

    subreddit = reddit.subreddit('wallstreetbets')


    # join all of this data together and then remove any duplicate values
    # rising_topics = subreddit.rising(limit=50)
    # trending_topics = subreddit.rising(limit=50)

    hot_topics = list(subreddit.hot(limit=10))

    potential_stock_names = [] 
    trending_stock_names =  []

    stock_names_list = pd.read_csv('stock-names-sheet.csv')['Name'].tolist()
    full_stock_names_list = pd.read_csv('stock-names-sheet.csv')['FullName'].tolist()


    d =  {"Name": stock_names_list,  "FullName": full_stock_names_list  }
    stock_df = pd.DataFrame(d)
    stock_df['Name'] = stock_df['Name'].astype('|S')

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
        trending_stocks_rank[stock] = {'comments': 0, 'upvote_ratio':0, 'score':0, 'downs':0, "ups": 0, "headlines": []}  



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
                new_ups = previousScoreCard['ups'] + post.ups
                new_downs = previousScoreCard['downs'] + post.downs
                previous_headlines = previousScoreCard['headlines']                
                head_line_dict = {"headline": post.title, "url": post.url}                          
                previous_headlines.append(head_line_dict)
                new_headlines = previous_headlines
                
                newScoreCard = {}
            
                newScoreCard['comments']  = new_comments
                newScoreCard['upvote_ratio']  = new_upvote_ratio
                newScoreCard['score']  = new_score
                newScoreCard['tickerName'] = stock
                newScoreCard['ups'] = new_ups
                newScoreCard['downs'] = new_downs
                newScoreCard['headlines'] = new_headlines

                trending_stocks_rank[stock] = newScoreCard 


    # list of dict
    stock_object_list = []
    sorted_stocks = []

    def insertion_sort_impl(L, *, key):
        for i in range(1, len(L)): # loop-invariant: `L[:i]` is sorted
            d = L[i]
            for j in range(i - 1, -1, -1): 
                if key(L[j]) <= key(d): 

                     break
                L[j + 1] = L[j]
            else: # `key(L[j]) > key(d)` for all `j`
                j -= 1
            L[j + 1] = d


    for stock in trending_stocks_rank:
        
        encoded_name = stock.encode('utf-8')
        # df.loc[df['column_name'] == 'value']
        full_row =  stock_df.loc[stock_df['Name'] == encoded_name  ]
        full_name =  list(full_row['FullName'])[0]
        new_stock_dict = {}
        raw_stock_object = trending_stocks_rank[stock]     
        new_stock_dict[full_name] = raw_stock_object     
        stock_object_list.append(new_stock_dict)


    insertion_sort_impl(stock_object_list, key=lambda x:  x[list(x.keys())[0]]['score']  ) # sort by `d` key
    stock_object_list.reverse()

    

def writeToFireBase():
    url = 'https://wsbsimplified-default-rtdb.firebaseio.com/'
    body = {'name': 'Maryja'}
    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(body), headers=headers)



if __name__ == "__main__":
    getData()


print("--- %s seconds ---" % (time.time() - start_time))















