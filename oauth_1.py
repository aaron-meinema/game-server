import requests
from requests_oauthlib import OAuth1

url = u'localhost:8080/oauth/token/request'

# client_key = u'...'
# client_secret = u'...'
# resource_owner_key = u'...'
# resource_owner_secret = u'...'
#
# headeroauth = OAuth1(client_key, client_secret,
#                      resource_owner_key, resource_owner_secret,
#                      signature_type='auth_header')

r = requests.get(url, headers={'Authorization': 'oauth_consumer_key="m748bxohupsrer5hqvaynfkhy8nlpyz8", '
                                                                  'oauth_signature_method="HMAC-SHA1",'
                                                                  'oauth_signature="",'
                                                                  'oauth_nonce="",'
                                                                  'oauth_timestamp="",'
                                                                  'oauth_version="1.0'})

