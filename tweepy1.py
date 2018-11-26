import tweepy
import time

print('This is tweepy Application')

CONSUMER_KEY = 'EPhctiinVPF7V6sl4cbEzivGW'
CONSUMER_SECRET = 'Jg3miQMB4FwJTXRdNLYKBPIYjQqhanN9UhKlM2JEF45nl4mZy8'
ACCESS_KEY = '2343006409-1eFj2Pb9FPG9xF77QEu7sx2Ss6vx9LW7Czkj6ri'
ACCESS_SECRET = 'TYDkL6S42zLczSULGq1du8PobvaE5qvKqxkg2bqrVXbxG'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)#api object to talk to twitter

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

'''mentions = api.mentions_timeline()
print(mentions[2].text)
for mention in mentions:
    print(str(mention.id))
    if 'thank' in mention.text.lower():
        print('found')
'''

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if 'thank' in mention.full_text.lower():
            print('found #helloworld!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    ' Hey I am Back to you!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)
