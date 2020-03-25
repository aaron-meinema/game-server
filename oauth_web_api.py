import requests
from requests_oauthlib import OAuth1
from urllib.parse import urlparse

resource_owner_key = 'rtxojvqglcd2m4f8n3pg6nhi1dviil00'
resource_owner_secret = 'bhzrf9y224nc2rlonf5z6urr0499n8ih'
client_key = 'm748bxohupsrer5hqvaynfkhy8nlpyz8'
client_secret = 'zz2z4zowvgyujqf38wcnzb0koqch7rx4'

request_token_url = 'http://127.0.0.1:8080/rest/V1/products/99212213'

oauth = OAuth1(client_key, client_secret=client_secret, resource_owner_key=resource_owner_key, resource_owner_secret=resource_owner_secret)
r = requests.get(url=request_token_url, auth=oauth)
# r.content
print(r.content)