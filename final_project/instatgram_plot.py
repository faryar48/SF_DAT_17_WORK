# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:51:00 2015

@author: faryarghaemi
"""

from instagram.client import InstagramAPI
import nltk
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt

api = InstagramAPI(access_token = access_token, client_secret = client_secret)
recent_media, next_ = api.user_recent_media(user_id = user_id, count = 100)
captions_array = []
for media in recent_media:
   captions_array.append(media.caption.text)


mediaIDArray = []
def getMediaID(recent_media):
    for media in recent_media:
        mediaIDArray.append(media.id)


def getMediaLikes(mediaIDArray):
    mediaLikesArray = []
    for media_id in mediaIDArray:
        mediaLikesArray.append(len(api.media_likes(media_id)))

    return mediaLikesArray

getMediaID(recent_media)
mediaLikesArray = getMediaLikes(mediaIDArray)


caption_sentiment = []
def stringToSentiment(array):
    for item in array:
        caption_sentiment.append(TextBlob(item).sentiment.polarity)


stringToSentiment(captions_array)
caption_sentiment_array = zip(captions_array, caption_sentiment)
sentiment_likes_array = zip(mediaLikesArray, caption_sentiment)
# print caption_sentiment_array
# print sentiment_likes_array

# plotting the caption sentiment against the numbers of likes to see if there is a correlation
plt.plot(mediaLikesArray, caption_sentiment, 'ro')

# relationships
# api.user_incoming_requests()
# api.user_follows(user_id)
# api.user_followed_by(user_id)
# api.follow_user(user_id)
# api.unfollow_user(user_id)
# api.block_user(user_id)
# api.unblock_user(user_id)
# api.approve_user_request(user_id)
# api.ignore_user_request(user_id)
# api.user_relationship(user_id)

# user follow/followed by relationship
# user_follows = api.user_follows(user_id)
# user_followed_by = api.user_followed_by(user_id)
# print user_follows, user_followed_by





# making unauthenticated requests
# api = InstagramAPI(client_id = client_id, client_secret = client_secret)
# popular_media = api.media_popular(count=20)
# for media in popular_media:
#     print media.images['standard_resolution'].url



