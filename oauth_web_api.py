import requests
import json
from requests_oauthlib import OAuth1

resource_owner_key = 'rtxojvqglcd2m4f8n3pg6nhi1dviil00'
resource_owner_secret = 'bhzrf9y224nc2rlonf5z6urr0499n8ih'
client_key = 'm748bxohupsrer5hqvaynfkhy8nlpyz8'
client_secret = 'zz2z4zowvgyujqf38wcnzb0koqch7rx4'

base_request_url = 'http://127.0.0.1:8080/rest/V1/'

oauth = OAuth1(client_key, client_secret=client_secret, resource_owner_key=resource_owner_key,
               resource_owner_secret=resource_owner_secret)

# request_token_url = 'http://127.0.0.1:8080/rest/V1/coupons/generate'
# request_token_url = 'http://127.0.0.1:8080/rest/V1/guest-carts/GDhzkXMSQVYT9kchcpc3QcCjkDF3txUD/coupons/40U2OX51368B'

x = {
    "couponSpec":
    {
        "rule_id": 1,
        "format": "string",
        "quantity": 1,
        "length": 0,
        "prefix": "string",
        "suffix": "string",
        "delimiter_at_every": 0,
        "delimiter": "string",
        "extension_attributes": { }
    }
}


def sendCouponRequest():
    code = {
        "couponSpec": {
            "rule_id": 97,
            "format": "",
            "quantity": 1,
            "length": 12,
            "prefix": "",
            "suffix": "",
            "delimiter_at_every": 0,
            "delimiter": "",
            "extension_attributes": {}
        }
    }

    ccode = {
      "giftCardAccountData": {
        "gift_cards": [
          "40U2OX51368B"
        ],
        "gift_cards_amount": 0,
        "base_gift_cards_amount": 0,
        "gift_cards_amount_used": 0,
        "base_gift_cards_amount_used": 0,
        "extension_attributes": {}
      }
    }

    coupon_link = 'coupons/generate'
    request_token_url = base_request_url + coupon_link

    # convert into JSON:
    y = json.dumps(code)

    r = requests.post(url=request_token_url, auth=oauth, data=y, headers={'Content-Type': 'application/json'})

    print(r.content)

    coupon = r.content.decode('utf-8')

    if coupon is None:
        return ""
    else:
        return coupon[2:-2]


def addCouponToCart(cart_id, coupon_code):
    if cart_id.isdigit():
        cart_link = 'cart/' + int(cart_id)
    else:
        cart_link = 'guest-carts/' + cart_id
    coupon_link = '/coupons/' + coupon_code

    request_token_url = base_request_url + cart_link + coupon_link

    r = requests.put(url=request_token_url, auth=oauth, headers={'Content-Type': 'application/json'})

    print(r.content)


def getCartItems(cart_id):
    request_token_url = base_request_url + 'carts/' + cart_id

    r = requests.put(url=request_token_url, auth=oauth, headers={'Content-Type': 'application/json'})
    return r.content

# sendCouponRequest()
# addCouponToCart('GDhzkXMSQVYT9kchcpc3QcCjkDF3txUD', '40U2OX51368B')
