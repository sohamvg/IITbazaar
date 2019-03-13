# IITbazaar
A web portal to buy and sell items in the campus made using django ( it is hosted on heroku at http://iit-bazaar.herokuapp.com/ ). Check at 13th March for complete experience.
# Main Features
* Login/Signup using your username and password. A User profile is created when you sign up. You can view items without logging in but you must be logged in to buy.
* Search bar for products and categories
* Shopping cart : add items to shopping cart to buy. You can also edit(add/delete) your shopping cart. After this, you checkout and proceed to buy items in your shopping cart.
* A unique transaction id is also generated for your purchases.
* Admin can see records of all users, products, sellers, order history etc.
* Security measures : Your password can't be too common or have less than 8 letters, unique transaction id, use of csrf token in forms
# To install dependencies
* django and python 3.6+ should be installed.
```
pip install django-reset-migrations
pip install django-phonenumber-field
pip install phonenumbers
pip install django-allauth
pip install pillow
```
# To run the website locally
From terminal, make sure you are in the same directory as manage.py
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Website will be hosted locally on http://127.0.0.1:8000/
# To try the site
**Admin account** at http://iit-bazaar.herokuapp.com/admin
username : admin   
password : pass_admin    
**User accounts**
user_1 : password_1   
user_2 : password_2     
