from db import db
from datetime import datetime, date, timedelta

class EventModel(db.Model):

    __tablename__ = "events"
    
    id = db.Column(db.Integer, primary_key=True)
    eventName = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now())