import tweepy
import json
import sys


def write_to_file(file, data):
    outfile = open(file, 'a+')
    outfile.write(json.dumps(data) + "\n")
    outfile.close()


def get_uid(line):
    line = line.rpartition("}")[0] + "}"
    if len(line) > 0:
        data = json.loads(line)
        uid = data["user"]["id"]
        return uid


# Key and access token to access Twitter API
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("\nUsage: python search_twitter.py <json_in_file_path> <out_file_path>\n")
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]

        # processing
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        # Interface creation
        api = tweepy.API(auth, wait_on_rate_limit=True)
        users = []
        with open(file1) as f:
            for line in f:
                try:
                    uid = get_uid(line)
                    if uid not in users:
                        users.append(uid)
                        for tweet in tweepy.Cursor(api.user_timeline, id=uid).items():
                            data = tweet._json
                            write_to_file(file2, data)
                except ValueError:
                    continue
                except:
                    continue
