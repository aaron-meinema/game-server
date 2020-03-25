import requests
from requests_oauthlib import OAuth1
from urllib.parse import urlparse

client_key = 'm748bxohupsrer5hqvaynfkhy8nlpyz8'
client_secret = 'zz2z4zowvgyujqf38wcnzb0koqch7rx4'


request_token_url = 'http://127.0.0.1:8080/oauth/token/request'
# print(request_token_url)

oauth = OAuth1(client_key, client_secret=client_secret)
r = requests.post(url=request_token_url, auth=oauth)
# r.content
print(r.content)