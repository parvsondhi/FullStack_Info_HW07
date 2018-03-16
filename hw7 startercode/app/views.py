from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm
from .forms import OrderForm
# Access the models file to use SQL functions


@app.route('/')
def index():
    return redirect('/trips')


@app.route('/login', methods=['GET', 'POST']) # You need to specify something here for the function to get requests
def login():
    # Here, you need to have logic like if there's a post request method, store the username and email from the form into
    # session dictionary
    if request.method == "POST":
        session['username']=request.form['username']
        session['email']=request.form['email']
    return redirect(url_for('index'))



@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('index'))

# template code

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    print(form)
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        models.insert_customer(data['first_name'], data['last_name'], data['company'], data['email'], data['phone'])
        print "jello"
        form.validate_on_submit()
        # Get data from the form
        # Send data from form to Database
        print "asdfasdfasdfasdf"
        return redirect('/customers')
    return render_template('customer.html', form=form)


@app.route('/customers')
def display_customer():
    orders = models.retrieve_orders()
    customers = models.retrieve_customers()
    # Retreive data from database to display
    return render_template('trips.html',
                            customers=customers,
                            orders=orders,
                            )

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    # Get data from the form
    # Send data from form to Database
    # return redirect('/customers')
    form = OrderForm()
    print(form)
    print(form.errors)
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        models.insert_order(data['name_of_part'], data['manufacturer_of_part'])
        if form.is_submitted():
            print "order form done"
        return redirect('/customers')
    return render_template('order.html', form=form)

@app.route('/orders')
def display_order():
    customers = models.retrieve_customers()
    orders = models.retrieve_orders()
    # Retreive data from database to display
    return render_template('trips.html',
                            orders=orders, customers=customers)
