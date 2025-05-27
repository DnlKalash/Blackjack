from mongoengine import Document, StringField, EmailField, ListField, FloatField, DictField, BooleanField

from django.contrib.auth.hashers import make_password, check_password

class User(Document):
    username = StringField(required=True, unique=True, max_length=150)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, max_length=128)
    last_result = ListField(FloatField(), default=[])
    

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

