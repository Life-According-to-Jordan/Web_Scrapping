#pip install python-twitter
import twitter 

consumer_key= 'YOUR KEY'
consumer_secret = 'YOUR CONSUMER SECRET'
access_token = 'YOUR ACCESS TOKEN'
access_secret = 'YOUR ACCESS SECRET'

api = twitter.Api(consumer_key=consumer_key, 
    consumer_secret = consumer_secret,
    access_token_key= access_token,
    access_token_secret=access_secret)

print(api.VerifyCredentials())

#get followers of user account 
followers = api.GetFollowers()

#tweeting to my professor for fun while I code
#post_update = api.PostUpdates(status='@tyleransom tweet sent from python #Econ5970')
#print(post_update)

#pull all followers User Names 
for u in followers:
    print(u.screen_name)




