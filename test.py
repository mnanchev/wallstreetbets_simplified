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

for topic in hot_topics:
    print(topic.title)
    # print(topic.selftext) actual text of reddit post 
    
    # print(topic.id)
    # print(topic.author)
    # print(topic.created_utc)
    # print(topic.score)
    # print(topic.upvote_ratio)
    # print(topic.url)











# ['author_fullname',  'category', 'clear_vote', 'clicked',  'comments', 'content_categories', 'created', 'created_utc',discussion_type', 'distinguished', 'domain', 'downs', 'downvote', 'duplicates', 'edit', 'edited', 'enable_inbox_replies', 'flair', 'fullname', 'gild', 'gilded', 'gildings', 'hidden', 'hide', 'hide_score', 'id', 'id_from_url', 'is_created_from_ads_ui', 'is_crosspostable', 'is_meta', 'is_original_content', 'is_reddit_media_domain', 'is_robot_indexable', 'is_self', 'is_video', 'likes', 'link_flair_background_color', 'link_flair_css_class', 'link_flair_richtext', 'link_flair_template_id', 'link_flair_text', 'link_flair_text_color', 'link_flair_type', 'locked', 'mark_visited', 'media', 'media_embed', 'media_only', 'mod', 'mod_note', 'mod_reason_by', 'mod_reason_title', 'mod_reports', 'name', 'no_follow', 'num_comments', 'num_crossposts', 'num_reports', 'over_18', 'parent_whitelist_status', 'parse', 'permalink', 'pinned', 'pwls', 'quarantine', 'removal_reason', 'removed_by', 'removed_by_category', 'reply', 'report', 'report_reasons', 'save', 'saved', 'score', 'secure_media', 'secure_media_embed', 'selftext', 'selftext_html', 'send_replies', 'shortlink', 'spoiler', 'stickied', 'subreddit', 'subreddit_id', 'subreddit_name_prefixed', 'subreddit_subscribers', 'subreddit_type', 'suggested_sort', 'thumbnail', 'title', 'top_awarded_type', 'total_awards_received', 'treatment_tags', 'unhide', 'unsave', 'ups', 'upvote', 'upvote_ratio', 'url', 'user_reports', 'view_count', 'visited', 'whitelist_status', 'wls']


# if a post has a stock ticker or name in the headline
# we can assume that the post is directly related to the trading of those
# stocks 

# we can find total engagement based off of stock names

# can find a list of headlines on a per stock basis



# what meaningful data is there to extract ? 
# any posts related to specific equities
# and then on a per stock basis list the total number of comments, likes, sentiment etc? 
# could find an aggreate upvote ratio


# we can verfiy stock names using the yfinance api 


# we can then assume that stocks with positive reviews or sentiment are going to rise in price in the near future
# and that


#  [{name: AMC, recentHeadlines: [.... , .... ] total_comments: 200,000, sentimentScore:Positive}]


# could find most trending stocks, order list by attention 

# commentSectionSentimentScore
# headlineSentimentScore



# maybe look into GME and try and back test these strategies 











