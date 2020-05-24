import sys

tweet_id = sys.argv[1].split('/')[-1]
url_string = f"https://twitter.com/search?q=-from:quotedreplies%20url:{tweet_id}&src=typed_query&f=live"
if tweet_id:
    print(f"copy the following url to your browser to view all quoted replies of your chosen tweet: \n\n{url_string}")
