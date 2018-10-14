from signupPatient import *
from pymodm import connect
import models
import datetime

connect("mongodb://vcm-6782.vm.duke.edu:27017/test")

def create_user(name, doctor, password):
    u = models.User(name, doctor, password)
    u.save()


def record_time():
    pass
