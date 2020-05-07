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

    def send_coupon_request(self, coupon_code_id):
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
        coupon = r.content.decode('utf-8')

        if coupon is None:
            return ""
        else:
            return coupon[2:-2]

    def add_coupon_to_cart(self, cart_id, coupon_code):
        if cart_id.isdigit():
            cart_link = 'carts/' + cart_id + '/coupons/' + coupon_code
        else:
            cart_link = 'guest-carts/' + cart_id + '/coupons/' + coupon_code

        request_token_url = self.base_request_url + cart_link
        r = requests.put(url=request_token_url, auth=self.oauth, headers={'Content-Type': 'application/json'})

        return r.content == b'true'

    def get_coupon_in_cart(self, cart_id):
        request_token_url = self.base_request_url + 'carts/' + cart_id + '/coupons'

        r = requests.get(url=request_token_url, auth=self.oauth, headers={'Content-Type': 'application/json'})
        return r.content

    def get_cart_items(self, cart_id):
        request_token_url = self.base_request_url + 'carts/' + cart_id

        r = requests.get(url=request_token_url, auth=self.oauth, headers={'Content-Type': 'application/json'})
        return r.content
