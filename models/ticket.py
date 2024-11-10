
from db import db
from datetime import datetime, date, timedelta

class TicketModel(db.Model):
    
    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now())


    