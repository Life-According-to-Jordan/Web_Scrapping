"""
virtualenv -p python 3 "folder_name" && cd "folder_name"
source bin/activate
python --version
pip install requests bs4
pip install python-twitter
"""
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

#get users and followers of user account
followers = api.GetFollowers()
#friends = api.GetFriends()

#tweeting to my professor
#post_update = api.PostUpdates(status='@tyleransom tweet sent from python #Econ5970')
#print(post_update)

filename = "Followers.csv"
f = open(filename, "w")
headers = "User_Screen_Name, \n"
f.write(headers)

#pull all followers User Names
for u in followers:
    print(u.screen_name)

    f.write(u.screen_name + "\n")

f.close




