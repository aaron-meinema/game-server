import requests
from requests_oauthlib import OAuth1

url = u'https://api.twitter.com/1/account/settings.json'

client_key = u'...'
client_secret = u'...'
resource_owner_key = u'...'
resource_owner_secret = u'...'

headeroauth = OAuth1(client_key, client_secret,
                     resource_owner_key, resource_owner_secret,
                     signature_type='auth_header')
r = requests.get(url, auth=headeroauth, headers={'Authorization': 'oauth_consumer_key --, '
                                                                  'oauth_signature_method  ,'
                                                                  'oauth_signature ,'
                                                                  'oauth_nonce ,'
                                                                  'oauth_timestamp ,'
                                                                  'oauth_version '})

