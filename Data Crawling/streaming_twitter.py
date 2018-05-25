from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Key and access token to access Twitter API
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


#Print crawled tweets
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':
    
    if len(sys.argv) != 1:
        print("\nUsage: python streaming_twitter.py [<GEOBOX>]\n")
    else:
        GEO = sys.argv[1]

        #Connect to Twitter Streaming API
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)

        #Filter tweets by location
        GEOBOX = GEO
        stream.filter(locations=GEOBOX)
