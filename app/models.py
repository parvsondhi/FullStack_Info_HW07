from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    trips = db.relationship('Trip', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tripname = db.Column(db.String(64), index=True, unique=True)
    destination = db.Column(db.String(64), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<User {}>'.format(self.tripname)
