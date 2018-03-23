from app import db
from datetime import datetime

class TripInvitation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    user = db.relationship('User',
        backref=db.backref('trip_invitations', lazy=True))

    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'),
        nullable=False)
    trip = db.relationship('Trip',
        backref=db.backref('trip_invitations', lazy=True))