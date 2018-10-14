from pymodm import fields, MongoModel


class User(MongoModel):
    # email = fields.EmailField()  # because primary_key is True,
    # we will need to query this field using the label _id
    username = fields.CharField(primary_key=True)
    name = fields.CharField(blank=True)
    doctor_status = fields.BooleanField()
    doctor = fields.CharField(blank=True)
    password = fields.CharField()
