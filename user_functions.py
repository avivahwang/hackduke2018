from signupPatient import *
from pymodm import connect
import models
# import datetime

connect("mongodb://vcm-6782.vm.duke.edu:27017/test")

def create_patient(username, doctor, password):
    u = models.User(username, [], False, doctor, password)
    u.save()
    print('Patient created!')


def create_doctor(username, name, password):
    u = models.User(username, name, True, '', password)
    u.save()
    print('Doctor created!')


def record_time():
    pass
