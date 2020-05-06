import requests
import json
from requests_oauthlib import OAuth1


class OauthWebAPI:
    base_request_url = 'http://127.0.0.1:8080/rest/V1/'

    def __init__(self, res_owner_key, res_owner_secret, client_key, client_secret):
        self.resource_owner_key = res_owner_key
        self.resource_owner_secret = res_owner_secret
        self.client_key = client_key
        self.client_secret = client_secret
        self.oauth = OAuth1(client_key, client_secret=client_secret, resource_owner_key=res_owner_key,
                            resource_owner_secret=res_owner_secret)

    def sendCouponRequest(self, coupon_code_id):
        # rule_id uit db
        code = {
            "couponSpec": {
                "rule_id": coupon_code_id,
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

        coupon_link = 'coupons/generate'
        request_token_url = self.base_request_url + coupon_link

        # convert into JSON:
        y = json.dumps(code)

        r = requests.post(url=request_token_url, auth=self.oauth, data=y, headers={'Content-Type': 'application/json'})

        print(r.content)

        coupon = r.content.decode('utf-8')

        if coupon is None:
            return ""
        else:
            return coupon[2:-2]

    def addCouponToCart(self, cart_id, coupon_code):
        if cart_id.isdigit():
            cart_link = 'cart/' + int(cart_id)
        else:
            cart_link = 'guest-carts/' + cart_id
        coupon_link = '/coupons/' + coupon_code

        request_token_url = self.base_request_url + cart_link + coupon_link

        r = requests.put(url=request_token_url, auth=self.oauth, headers={'Content-Type': 'application/json'})

        print(r.content)

        if r.content:
            return True
        else:
            return False

    def getCartItems(self, cart_id):
        request_token_url = self.base_request_url + 'carts/' + cart_id

        r = requests.put(url=request_token_url, auth=self.oauth, headers={'Content-Type': 'application/json'})
        return r.content

        # sendCouponRequest()
        # addCouponToCart('GDhzkXMSQVYT9kchcpc3QcCjkDF3txUD', '40U2OX51368B')
