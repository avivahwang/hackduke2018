import datetime
import models
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from main import *

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/api/patient_base", methods=["POST"])
    def patient_data():
        try:
            r = request.get_json()
            username = r["username"]
            doctor = r["doctor"]
            password = r["password"]
            patient = create_patient(username, doctor, password)
            return "Patient data added."
        except:
            return "Not a valid input!"


@app.route("/api/doctor_base", methods=["POST"])
    def doctor_data():
        try:
            r = request.get_json()
            username = r["username"]
            name = r["name"]
            password = r["password"]
            doctor = create_doctor(username, name, password)
            return "Doctor data added."
        except:
            return "Not a valid input!"
