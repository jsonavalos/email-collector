from flask import Flask, request, render_template, jsonify, redirect, url_for
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/URL"
mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("home.html")

# Redirect users to original link
@app.route("/api/s/<short_name>")
def home2(short_name):
    response = mongo.db.links.find({"short_link": short_name})  # cursor
    if response.count() == 0:  # if empty ,then database doesn't contain link
        return "Link has not been shorted"
    original_link = list(response)[0]['original_link']
    print(original_link)
    # redirect to short name stored in database
    return redirect(original_link)

# Get original link from user
@app.route("/api/make_short", methods=["POST"])
def make_short():
    body = request.json
    
    url = 'https://jsonavalos.run-us-west2.goorm.io' + '/api/s/manuelitoavalos'
    mongo.db.links.insert({'short_link': url , 'original_link': body['link']})
    return jsonify(original_link=body['link'], short_link='manuelitoavalos')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
