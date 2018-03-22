from functools import wraps
from flask import flash, abort
from flask_login import current_user
from app.models import TripInvitation


def inject_trip_invitation(func):
    @wraps(func)
    def decorated_function(id, *args, **kwargs):
        trip_invitation = TripInvitation.query.filter_by(user_id=current_user.id, trip_id=int(id)).first()
        if trip_invitation is None:
            flash('The trip does not exists!', 'error')
            return abort(404)

        return func(trip_invitation, *args, **kwargs)

    return decorated_function