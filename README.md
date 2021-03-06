# IITbazaar
A web portal to buy and sell items in the campus made using django ( it is hosted on heroku at http://iit-bazaar.herokuapp.com ). 
## Features
* Login/Signup using your username and password. A User profile is created when you sign up. You can view items without logging in but you must be logged in to buy.
* When you sign in, you are directly logged in.
* Search bar for products and categories
* View details of products, categories and sellers.
* Shopping cart : add items to shopping cart to buy. You can also edit(add/delete) your shopping cart on the go. After this, you can checkout and then redirected to the payent page from where proceed to buy items in your shopping cart.
* A unique transaction id is also generated for your purchases. Date and time of all transactions is also stored in the database.
* Admin can see records of all users, products, sellers, order history etc.
* Security measures : Your password can't be too common or have less than 8 letters, unique transaction id, use of csrf token in forms
## To run the website locally
### Installing dependencies
* django and python 3.6+ should be installed.
```
pip install django-reset-migrations
pip install django-phonenumber-field
pip install phonenumbers
pip install django-allauth
pip install pillow
```
From terminal, make sure you are in the same directory as manage.py
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Website will be hosted locally on http://127.0.0.1:8000/
## Try the website
At http://iit-bazaar.herokuapp.com/admin,

- **Admin account**
  - username : `admin`   
  - password : `pass_admin`        
