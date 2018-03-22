from functools import wraps
from flask import redirect, flash, abort
from flask_login import current_user
from app.models import Trip, TripInvitation


def user_is_invited_to_trip(func):
    @wraps(func)
    def decorated_function(trip, *args, **kwargs):
        if TripInvitation.query.filter_by(user_id=current_user.id, trip_id=trip.id).first():
            return func(trip, *args, **kwargs)

        flash('You do not have access to this trip!', 'error')
        return abort(403)

    return decorated_function