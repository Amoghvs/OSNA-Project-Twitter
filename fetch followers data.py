#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 14:31:43 2020

@author: amogh
"""

import tweepy
import csv

twitter_handle = 'amoghvs'


consumer_key='x'
consumer_secret='x'


access_token='x'
access_secret='x'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)



users = tweepy.Cursor(api.followers, screen_name=twitter_handle, count = 200).items()

for u in users:
    screenName = u.screen_name
    name = u.name
    location = u.location
    print(screenName)
    
