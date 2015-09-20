__author__ = 'abhilash'
import datetime
from SimpleApi.config.application_config import mongo_db

class Product(mongo_db.Document):
    name = mongo_db.StringField(max_length=60)
    publication_date = mongo_db.DateTimeField(default=datetime.datetime.now)
