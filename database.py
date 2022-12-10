from peewee import *
from datetime import date
from flask_login import UserMixin

db = peewee.MySQLDatabase(
    database = "studio_guide_prototype",
    user = ""
)
