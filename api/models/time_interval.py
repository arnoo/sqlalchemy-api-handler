from sqlalchemy import Column, DateTime
from sqlalchemy_api_handler import ApiHandler

from api.utils.database import db


class TimeInterval(ApiHandler,
                   db.Model):

    end = Column(DateTime)

    start = Column(DateTime)
