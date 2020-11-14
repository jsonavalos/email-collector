from flask import Flask, request, render_template, jsonify, redirect, make_response
from flask_pymongo import PyMongo
import random
import string
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/URL"
mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("home.html")


# Get original link from user to make short
@app.route("/api/make_short", methods=["POST"])
def make_short():
    body = request.json
    if mongo.db.links.find({"original_link": body['link']}).count() != 0:
        res = mongo.db.links.find({"original_link": body['link']})
        url = request.url_root + 'api/s/' + list(res)[0]['short_link']
        return make_response(jsonify(original_link=body['link'], short_link=url))
    result_str = unique_string()
    url = request.url_root + 'api/s/' + result_str
    mongo.db.links.insert({'short_link': result_str, 'original_link': body['link']})
    return make_response(jsonify(original_link=body['link'], short_link=url))


# Redirect users to original link
@app.route("/api/s/<short_name>")
def home2(short_name):
    response = mongo.db.links.find({"short_link": short_name})  # cursor
    if response.count() == 0:  # if empty ,then database doesn't contain link
        return jsonify(original_link='', short_name='')
    original_link = list(response)[0]['original_link']
    return redirect(original_link)


# Delete an entry
@app.route("/api/delete", methods=['DELETE'])
def delete():
    body = request.json
    link_to_delete = body['link_to_delete'] # can be either the original or short one
    substring = '/api/s/'
    if substring in link_to_delete:
        short_link = link_to_delete[-5:]
        print(short_link)
        mongo.db.links.remove({"short_link": short_link}, 1)
    mongo.db.links.remove({"original_link": link_to_delete}, 1)
    return jsonify(success=True)


def unique_string():
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(5))
    while mongo.db.links.find({"short_link": result_str}).count() == 1:  # to prevent duplicates
        result_str = ''.join(random.choice(letters) for i in range(5))
    return result_str


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
