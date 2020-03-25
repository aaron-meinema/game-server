from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

high_score = 0


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
        # subcategory moet naar de database gecheckt worden, vervolgens de origin controleren. dan user etc.
        return status.HTTP_405_METHOD_NOT_ALLOWED
    else:
        if score > high_score:
            high_score = score
        return "high score is " + str(high_score) + " your score is: " + str(score), status.HTTP_200_OK


@app.route("/oauth", methods=['GET', 'POST', 'PUT'])
def oauth_magento_keys():
    print(request.data)

    return str(0), status.HTTP_200_OK


if __name__ == "__main__":
    app.run(debug=True)