# Autenticação tweepy

#AOthHandler

API_key = ''
API_key_secret = ''

#set_access_token

access_token = ''
access_token_secret = ''

import tweepy
import autenticacao as aut

auth = tweepy.OAuthHandler(aut.API_key, aut.API_key_secret)
auth.set_access_token(aut.access_token, aut.access_token_secret)

api = tweepy.API(auth)

#Envia o tweet
tweet = 'EXEMPLO DE TWEET'

try:
    api.update_status(tweet)
    print(tweet)
except tweepy.TweepyException as e:
    print(e.reason)

filename = 'DIRETORIO DA IMAGEM'
api.update_profile_image(filename)

api.update