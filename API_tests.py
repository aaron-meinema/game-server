import requests
import oauth_web_api

m2_api = oauth_web_api
# opzoeken welk cart_id ik heb, of via api cart aanmaken en aan dit id geven

def test_category_game_finished_add_to_cart_response_200():
    response = requests.post('http://localhost:3000/didi/500/4')
    assert response.status_code == 200


def test_category_game_finished_add_to_cart_wrong_category_response_405():
    response = requests.post('http://localhost:3000/didi/500/4')
    assert response.status_code == 405


def test_category_game_finished_add_to_cart_low_score_response_204():
    response = requests.post('http://localhost:3000/didi/1/4')
    assert response.status_code == 204


def test_category_game_finished_add_to_cart_low_score_response_20():
    response = requests.post('http://localhost:3000/didi/1/4')
    assert response.status_code == 204


def test_category_game_finished_add_to_cart_coupon_added_to_cart():
    response = requests.post('http://localhost:3000/didi/500/4')
    cart_items = m2_api.getCartItems('4')
    # opzoeken wat de query hiervoor is
    assert cart_items.currency


def test_length_coupon_code_assert_12():
    # add coupon via m2_api en dan dit testen door /carts/id


def test_category_game_finished_add_to_cart_score_200_2procent_discount_in_cart():
    # skip


# test_database_filled_after_score_completed - score, cart_id, coupon