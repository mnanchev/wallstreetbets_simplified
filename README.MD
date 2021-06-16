

Objective: To automate the functionality of wsb reddit form

How People Use WSB:

1. read through different posts

2. people find hot stocks to invest in 

3. people make money in the short term


How to Automate This:

1. Eliminate the need to manually read through the subreddit to find the stock you need
/ are currently trending and bullish(ideally as early as possible to get the most gains)
2. Calculate rankings on a per stock basis to present to user
3. use a brokerage api to execute trades automatically
4. Divest after realizing x gains ....


Steps:
1. Find a way to extract stock names / tickers from headlines 
2. create a list of all stock names found per API request 
3. Calculate rankings of stocks in list based on postiive interaction 


Step 1 :  
 - Pull stock names from headlines, verify that stock actually exists, then add to a list of stock names trending in the current API pull 
 - tickers are usually 3 to 4 capital letters 
 - iterate through x characters, check if all caps, if so make api request to verify , if true add to list of stock names trending in wsb 

- ticker name criteria: 1 - 7 characters, could start with a $ sign, ignore .s 



- Bug: could pull valid ticker names not related to article


Current Task:
- validate ticker names using the excel sheet
- also import the excel names using pandas for verification 






