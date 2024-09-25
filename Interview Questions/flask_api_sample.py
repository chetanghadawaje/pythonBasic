from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET',])
def home():
    if request.method == "GET":
        return jsonify({"Message": "Get API Call..."})
    return jsonify({"Message": "API call..."})


if __name__ == "__main__":
    app.run()
