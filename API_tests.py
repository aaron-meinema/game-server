import requests
from oauth_web_api import OauthWebAPI
import database.db_queries as db

m2_api = OauthWebAPI('rtxojvqglcd2m4f8n3pg6nhi1dviil00', 'bhzrf9y224nc2rlonf5z6urr0499n8ih',
                     'm748bxohupsrer5hqvaynfkhy8nlpyz8', 'zz2z4zowvgyujqf38wcnzb0koqch7rx4')

cart_id = 20


def test_game_finished_coupon_added_to_cart():
    response = requests.post('http://localhost:3000/didi/500/20')
    assert response.status_code == 201


def test_cart_id_and_coupon_added_in_db():
    assert db.select_coupon_with_cart_id(cart_id, 'didi') is not None


def test_coupon_code_in_cart():
    assert m2_api.get_coupon_in_cart(cart_id) is not None
