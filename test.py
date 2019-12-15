# def matched(ip_str):
#     stk=list(ip_str)
#     n=0
#     while n<=len(stk)-1:
#         if stk[n] == '(':



# def main():
#     matched('()')

# if __name__ == "__main__":
#     main()    


# #({()}    

import tweepy
consumer_key = "gkXDbvoLW9lfXCxcmxXdQQIfD"
consumer_secret = "DEwkj6fJQMB8tVV78heN1ov5m6c17H4s79ECuscFebbjtdS268"
access_token = "21473521-ONa3auOC8soh9F90IVFtQdlAJZpeNnfLFy2I74wfE"
access_token_secret = "Crw4QMLZhHfqcDPPhOnbM7VnlY1H7WFH7UfF9BvChPCIp"



# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 


# Creating the API object while passing in auth information
api = tweepy.API(auth)

# The search term you want to find
query = "(ex-convicts OR ex-convict OR ex-cons OR conviction) AND employment"
# Language code (follows ISO 639-1 standards)
language = "en"

# Calling the user_timeline function with our parameters
# results = api.search(q=query, lang=language, tweet_mode="extended",filter="retweets")
# print(results)

# tweets = [[tweet.full_text] for tweet in results]
# print(tweets)
# foreach through all tweets pulled
myfile = open('tweets.txt', 'w')
# n=1
# for tweet in results: 
    
# #    printing the text stored inside the tweet object
#     # print('\n') 
#     # print(tweet.user.screen_name,"Tweeted:",tweet.full_text)
# #     tweets = [[tweet.full_text] for tweet in tweet]
#     # print(tweet._json['full_text']) 
#     var=tweet._json['full_text']
#     print(var)
#     myfile.write("Tweet Number: {0}: {1}\n".format(n,var))
#     print(n)
#     n+=1

# # myfile.close()
# # text_file.close()


# query = 'python'
max_tweets = 3
searched_tweets = [json for json in tweepy.Cursor(api.search, q=query, tweet_mode="extended", filter="retweets", lang=language).items(max_tweets)]
tweets=searched_tweets[0]._json
# if tweets['retweeted'] and 'RT @' in tweets['']:
print('Mayank')
# print(tweets)
print(tweets['retweeted_status']['full_text'])

# n=1
# for tweet in tweets: 
    # print(tweet)    
# #    printing the text stored inside the tweet object
#     # print('\n') 
#     # print(tweet.user.screen_name,"Tweeted:",tweet.full_text)
# #     tweets = [[tweet.full_text] for tweet in tweet]
#     # print(tweet._json['full_text']) 
var=tweets['retweeted_status']['full_text']
#     print(var)
myfile.write("Tweet Number:: {0}\n".format(var))
#     print(n)
# n+=1

# myfile.close()