from functools import wraps
from flask import redirect, flash, abort
from flask_login import current_user
from app.models import Trip


def trip_owned_by_user(func):
    @wraps(func)
    def decorated_function(id, *args, **kwargs):
        trip = Trip.query.filter_by(id=int(id)).first()
        if trip is None:
            flash("The trip does not exists")
            return abort(404)

        if trip.user_id != current_user.id:
            flash("You do not have access to this trip!")
            return abort(403)

        return func(trip, *args, **kwargs)

    return decorated_function