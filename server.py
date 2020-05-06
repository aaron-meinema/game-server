import oauth_web_api
import database.db_queries as db

from flask import request
from flask_cors import CORS
from flask_api import FlaskAPI, status

app = FlaskAPI(__name__)
CORS(app)
# m2_api = oauth_web_api


@app.route("/game_finished/<int:score>/", methods=['POST'])
def game_finished(score):
    global high_score
    if score > high_score:
        high_score = score

    return str(score), status.HTTP_201_CREATED


@app.route("/get_high_score", methods=['GET'])
def get_high_score():
    global high_score

    return str(high_score), status.HTTP_200_OK


@app.route("/<string:subcategory>/<int:score>", methods=['POST'])
def category_game_finished(subcategory, score):
    global high_score
    if request.environ['HTTP_ORIGIN'] is not None:
        print(request.environ['HTTP_ORIGIN'])

    if subcategory != 'test':
        return status.HTTP_405_METHOD_NOT_ALLOWED
    else:
        if score > 100:
            high_score = score
            coupon = m2_api.sendCouponRequest()
            if coupon == "":
                return '-1', status.HTTP_200_OK
            else:
                return str(coupon), status.HTTP_201_CREATED
        else:
            return '-1', status.HTTP_200_OK


@app.route("/<string:shop>/<int:score>/<string:cart_id>", methods=['POST'])
def category_game_finished_add_to_cart(shop, score, cart_id):
    if request.environ['HTTP_ORIGIN'] is not None:
        shop_id, res_owner_key, res_owner_secret, client_key, client_secret, coupon_code_id = \
            get_code_id_corresponding_to_score(request.environ['HTTP_ORIGIN'], shop, score)
        if coupon_code_id is not None:
            m2_api = oauth_web_api.OauthWebAPI(res_owner_key, res_owner_secret, client_key, client_secret)
            coupon = get_coupon_for_cart_id(cart_id, m2_api, coupon_code_id, shop_id, score)
            if coupon is None:
                return '-1', status.HTTP_204_NO_CONTENT
            else:
                if addCouponToCart(m2_api, coupon, cart_id, shop_id):
                    return status.HTTP_201_CREATED
                else:
                    return str(coupon), status.HTTP_204_NO_CONTENT
    else:
        return status.HTTP_403_FORBIDDEN
                # if m2_api.addCouponToCart(cart_id, coupon):
                #     # insert statement
                #     return str(coupon), status.HTTP_201_CREATED
                # else:
                #     # insert statement
                #     return str(coupon), status.HTTP_304_NOT_MODIFIED

    # if shop != 'didi':
    #     return status.HTTP_405_METHOD_NOT_ALLOWED
    #     # subcategory moet naar de database gecheckt worden, vervolgens de origin controleren. dan user etc.
    # else:
    #     if score > 100:
    #         high_score = score
    #         coupon = m2_api.sendCouponRequest()
    #         if coupon == "":
    #             return '-1', status.HTTP_204_NO_CONTENT
    #         else:
    #             if m2_api.addCouponToCart(cart_id, coupon):
    #                 return str(coupon), status.HTTP_201_CREATED
    #             else:
    #                 return str(coupon), status.HTTP_304_NOT_MODIFIED
    #     else:
    #         return '-1', status.HTTP_204_NO_CONTENT


def addCouponToCart(m2_api, coupon, cart_id, shop_id):
    if m2_api.addCouponToCart(cart_id, coupon):
        insert_coupon_with_cart_id_in_db(cart_id, shop_id, coupon)
    else:
        insert_coupon_with_cart_id_in_db(cart_id, shop_id, coupon, False)


def get_code_id_corresponding_to_score(origin, shop_id, score):
    return db.get_coupon_id_webshop(origin, shop_id, score)


def get_coupon_for_cart_id(cart_id, m2_api, coupon_code_id, shop_id, score):
    generated_coupon = check_cart_id_for_coupon(cart_id, shop_id)
    if generated_coupon is not None:
        return generated_coupon
    else:
        insert_score_in_db(score, shop_id)
        return m2_api.sendCouponRequest(coupon_code_id)


def check_cart_id_for_coupon(cart_id, shop):
    return db.select_coupon_with_cart_id(cart_id, shop)


def insert_score_in_db(score, shop_id):
    db.insert_score_with_shop(score, shop_id)


def insert_coupon_with_cart_id_in_db(cart_id, shop, coupon_code, added=True):
    db.insert_cart_id_with_coupon(cart_id, shop, coupon_code, added)


if __name__ == "__main__":
    app.run(debug=True)
