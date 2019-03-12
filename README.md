# IITbazaar
A web portal to buy and sell items in the campus made using django ( it is hosted on heroku at http://iit-bazaar.herokuapp.com/ ). Check at 13th March for complete experience.
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
**User account**
username : user_1
password : password_1
