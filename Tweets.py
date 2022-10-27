# Twitter - Tweet extractor

"""
Requirements:
- pip install snscrape

Possible to extract info without a Dev account. Eg.:
- date, content, user, displayname, user description and much more
"""

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from:WarpRecords)" # Use the link below to make search term more advanced:
# https://twitter.com/search-advanced
# example tweets:
## "(from:PolestarCars)"
## "sustainability (from:elonmusk) until:2022-10-27 since:2010-01-01"

tweets = []
limit = 100 # how many tweets you want
for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    #print(vars(tweet))
    #break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)