**REQUIREMENTS**

 * As a user of this webpage I want to be able to enter customer information

 * Along with the customer information, I should also be able to add address information for
 the customer

 * On home.html, I shoulsdad be able to place orders for customers.

-------

  * models.py : insert_address method, takes customer_id
    * Q? - How to make customer_id available to address form?
      * A: 'add address' link in customer listing
    * Q? - Display customer information when adding addresses
    * case - no customer_id -> error (customer not in database)


 * home.html: order form (name of part, manufacturer of part, customer)

 * schema.sql:
  √ Create db Statements
  √ insert dummy data on create
  *

**NEXT**
  √ Database Create Statement and dummy data: 1 customer, 1 address, 1 order
  √ update '/' Homepage re-direct
  * Forms
  *

  √ customer.html:form:CreateCustomer (fname, lname, company, email, phone)
  √ models.py : insert_customer method
