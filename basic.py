from main import *
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/api/user_base", methods=["POST"])
def user_data():
    r = request.get_json()
    name = r["name"]
    doctor = r["doctor"]
    password = r["password"]
    user =  create_user(name, doctor, password)
    return "User data receieved"
