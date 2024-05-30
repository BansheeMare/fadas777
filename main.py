from flask import Flask, jsonify, json, request, Response, send_file
app = Flask(__name__)


@app.route("/")
def home():
    return send_file('index.html')

if __name__ == "__main__":
    app.run(debug=True)