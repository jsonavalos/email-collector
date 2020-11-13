from flask import Flask, request, render_template, jsonify
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

# Redirect users to original link
@app.route("/api/s/<short_name>")
def home2(short_name):
    # redirect to short name stored in database
    return "home 2 route"

# Get original link from user
@app.route("/api/make_short", methods=["POST"])
def make_short():
    body = request.json
    return jsonify(original_link=body['link'], short_link="Jason Avalos")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
