from flask import render_template
from app import app
from .forms import LoginForm


@app.route('/')
def index():
    form = LoginForm()
    if form.validate_on_submit():
        return "Submitted"

    return render_template('index.html')

