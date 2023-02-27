
from flask import jsonify, make_response

def home():
    return make_response(jsonify({"messgae":"ok"}), 200)