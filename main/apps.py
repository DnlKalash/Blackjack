from django.apps import AppConfig
from mongoengine import connect

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        connect(
            db='mydatabase',
            host='mongodb+srv://dnlkalash322:22259820Dnl@cluster0.wupf9an.mongodb.net/mydatabase?retryWrites=true&w=majority'
        )
