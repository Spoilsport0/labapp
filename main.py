from flask import Flask, make_response

app = Flask(__name__)

@app.route("/api/v1/hello-world-4")
def hello_world():
    return make_response("Hello World 4", 200)