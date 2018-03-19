## FullStack_Info_HW07
FullStack_Info_HW07 * Mega Lab

# MM100
* User must be able to login (“login” page)
  * [X] User Object and db query
  * [X] login required pages and redirects
  * [X] Forms and validation

* After the user logins in, they are taken to a page that displays the trips they
are a part of. (we’ll call this the “trips” page)
  * [X] Login Form
  * [X] Get trips for logged in user
  * [X] Display on /index
  * [X] Template styling
* On the trips page, there should be a button that allows the user to create a trip (“create trip” page)
  * [X] update template html
  * [X] /create-trip route
* On the create trip page, users should be allowed to create a trip with the minimum of the following information (trip name, destination, and ONE friend)
* Upon creation, this information must be stored in a database
  * [X] Create Trip form object, [DEBUG] friend_id manual input
  * [.] Form handler logic in route
  * [.] ! Write trip to database
  * [X] html template update


# MM200
* The friend on the trip must be a user in the system
  * We recommend adding the friend via your form using a dropdown
  * [ ] pre-populate dropdown menu on Create Trip form
  * [ ] M2M table for friends + trips. Update Database Migrations
  * [ ] Query for invited trips.
* Each user can see the trips they are a part of on their trips page
  * [ ] Add second table to template for invited trips
  * [ ] Update route to get and display invited trips
* The user should be able to delete any trip
  * You can use any method you want, but we recommend using jQuery to remove elements from the DOM and make an ajax call to a method to delete information from the table
  * [ ] Add Delete button to table
  * [ ] add delete_trip/<value> route
    * [ ] implement delete + reload || Ajax remove and trigger delete






# Extra Credits
* Signup
* Logout
* Embedded Google Map

Michelle and Peter

# To Do:
* implement logout and login_required
* display trips on index page
