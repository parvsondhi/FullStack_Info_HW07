from app import db
from datetime import datetime
from app.models import User

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, nullable=False)
    destination = db.Column(db.String(128), index=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    owner = db.relationship('User',
        backref=db.backref('trips', lazy=True))
    
    guests = db.relationship('User', secondary='trip_invitation', lazy='subquery',
        backref=db.backref('invited_trips', lazy=True))

    def invitable_users(self):
        participating_users = list(map(lambda user: user.id, self.guests))
        participating_users += [self.user_id]
        return User.query.filter(~User.id.in_(participating_users)).all()
