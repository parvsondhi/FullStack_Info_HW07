from functools import wraps
from flask import flash, abort
from app.models import Trip


def inject_trip(func):
    @wraps(func)
    def decorated_function(id, *args, **kwargs):
        trip = Trip.query.filter_by(id=int(id)).first()
        if trip is None:
            flash("The trip does not exists!")
            return abort(404)

        return func(trip, *args, **kwargs)

    return decorated_function