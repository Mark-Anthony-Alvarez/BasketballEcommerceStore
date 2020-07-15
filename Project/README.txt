
------------- THE 4TH QUARTER -------------

INTRO
~~~~~

This web application is an online e-commerce store that sells basketball products.
If a user wants to shop for a basketball, NBA Jerseys or sports wear such as T-shirts,
then they can easily visit this website and place an order of the items they desire.
The homepage shows the items available that they may purchase and add to their cart before
clicking checkout on the order page. If the user wants to delete an item, they may do so.
The user also has the ability to search via text in the upper right hand side of the page
in order to look for specific items if they would like.

TECHNOLOGIES
~~~~~~~~~~~~~

The technologies used in this web app are: Flask-WTForms, SQLite, SQLAlchemy, Python, HTML and Bootstrap.
Very little javascript, jquery and css has been used. Most of the styling is being used with bootstrap.
Flask has been used to incorporate python code in our HTML pages using jinja syntax, so that one page can 
be used to display the items after a category has been chosen by the user. Python was used to create classes and functions that will
help make the web application dynamic. SQLite has been used to make 4 data tables. Orders, Items, Categories and order details.


LAUNCH APP
~~~~~~~~~~~
In order to launch this application you have to go to your terminal whether you are using
the built-in terminal in VSCode or not, you must go to the Project557 directory, and then procede with
using the command 'python3 run.py' and the app should be launched.
The app will run on your local machine at ip address: 127.0.0.1:5000 and you can
copy and paste that address into your browser to view and use the app.
I have included an admin.py page that would seed the database.

An issue I have come across while using chrome browser, if not using incognito mode, the checkout form
will not work properly, and will render the 404.html because the session needs to be a new one.

VIDEO
~~~~~~
https://youtu.be/LfMeDzJ_rX4