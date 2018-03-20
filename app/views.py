from flask import request, Flask, session, redirect, url_for, escape, request, render_template
from app import app, models, db
from .forms import CustomerForm, OrderForm
# Access the models file to use SQL functions
from models import insert_customer_data, insert_order_data, retrieve_customers, retrieve_orders

@app.route('/')
def index():
    if 'username' in session:
        return render_template('trip.html', username=escape(session['username']))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        print request.form
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/create_trip')
def create_trip():
    return 'Create trip'

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
