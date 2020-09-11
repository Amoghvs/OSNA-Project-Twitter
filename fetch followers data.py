#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 14:31:43 2020

@author: amogh
"""

import tweepy
import csv

twitter_handle = 'amoghvs'


consumer_key='omNNShV46ijfz4cjoYnnwSyaP'
consumer_secret='U4zOGPcMCMKdYGTehzIDKklsyBmVkp0M8sqJKAktytZ1LY3DtV'


access_token='295100676-HDCg2pwKy7qa0CsFmClIPhaqr4LhGHhR4PC8NYCm'
access_secret='nARxQP59EuKCuaJNiInV00vvSTif42BboCzUl9ZR9xpQ9'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)



users = tweepy.Cursor(api.followers, screen_name=twitter_handle, count = 200).items()

for u in users:
    screenName = u.screen_name
    name = u.name
    location = u.location
    print(screenName)
    
