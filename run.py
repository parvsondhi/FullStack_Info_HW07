from app import app, db
from app.models import User, Trip

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Trip': Trip}


# app.run(debug=True, host="0.0.0.0", port=8081)
