'''
CREATING A NEW DATABASE
-----------------------
Read explanation here: https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

In the terminal navigate to the project folder just above the miltontours package
Type 'python' to enter the python interpreter. You should see '>>>'
In python interpreter type the following (hitting enter after each line):
    from miltontours import db, create_app
    db.create_all(app=create_app())
The database should be created. Exit python interpreter by typing:
    quit()
Use DB Browser for SQLite to check that the structure is as expected before 
continuing.

ENTERING DATA INTO THE EMPTY DATABASE
-------------------------------------

# Option 1: Use DB Browser for SQLite
You can enter data directly into the cities or tours table by selecting it in
Browse Data and clicking the New Record button. The id field will be created
automatically. However be careful as you will get errors if you do not abide by
the expected field type and length. In particular the DateTime field must be of
the format: 2020-05-17 00:00:00.000000
# Option 2: Create a database seed function in an Admin Blueprint
See below. This blueprint needs to be enabled in __init__.py and then can be 
accessed via http://127.0.0.1:5000/admin/dbseed/
Database constraints mean that it can only be used on a fresh empty database
otherwise it will error. This blueprint should be removed (or commented out)
from the __init__.py after use.

Use DB Browser for SQLite to check that the data is as expected before
continuing.
'''

from flask import Blueprint
from . import db
from .models import Category, Item, Order
import datetime


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database


@bp.route('/dbseed/')
def dbseed():
    category1 = Category(name='Sportswear', image='redshirt.jpg',
                         description='''Active sportswear for your basketball needs, whether you are practicing or if its for social play.''')
    category2 = Category(name='NBA Jerseys', image='embiid.jpg',
                         description='''High quality premium NBA Jerseys to support your favorite team.''')
    category3 = Category(name='Basketballs', image='bballjordan1.jpg',
                         description='''Indoor and outdoor basketballs for your street basketball games and indoor play.''')

    try:
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.commit()
    except:
        return 'There was an issue adding the category of products in dbseed function'

    i1 = Item(category_id=category1.id, image='redshirt.jpg', price=19.99,
              name='Red T Shirt',
              description='Active wear Adidas basketball shirt, perfect for us in a practice scenario.')
    i2 = Item(category_id=category1.id, image='shirtitem2.jpg', price=49.90,
              name='Long Sleeve Shirt',
              description='Active long sleeve shirt so you can play outdoors even during the colder seasons.')
    i3 = Item(category_id=category1.id, image='shirtitem3.jpg', price=19.50,
              name='White T Shirt',
              description='A slime fit white t shirt with a beautiful design of the basketball on front side. ')
    i4 = Item(category_id=category1.id, image='shirtitem4.jpg', price=22.99,
              name='Gray basketball T Shirt',
              description='A trendy basketball t-shirt that can be used for practicing but can also be sued for casual occasions.')
    i5 = Item(category_id=category2.id, image='embiid.jpg', price=99.00,
              name='Joel Embiid NBA Jersey',
              description='Premium quality authentic jersey of the player Joel Embiid from the Philadehlphia 76ers.')
    i6 = Item(category_id=category2.id, image='embiid.jpg', price=99.99,
              name='NBA Jersey',
              description='Jersey2')
    i7 = Item(category_id=category2.id, image='embiid.jpg', price=100.00,
              name='NBA Jersey',
              description='Jersey3')
    i8 = Item(category_id=category2.id, image='embiid.jpg', price=110.00,
              name='NBA Jersey',
              description='Jersey4')
    i9 = Item(category_id=category3.id, image='bballjordan1.jpg', price=149.99,
              name='Indoor Basketball',
              description='Indoor basketball meant for use for practice and gametime on the hardwood basketball setting.')
    i10 = Item(category_id=category3.id, image='bballproduct1.jpg', price=199.95,
               name='Outdoor Basketball',
               description='Basketball meant for the outdoor and street ball games.')

    try:
        db.session.add(i1)
        db.session.add(i2)
        db.session.add(i3)
        db.session.add(i4)
        db.session.add(i5)
        db.session.add(i6)
        db.session.add(i7)
        db.session.add(i8)
        db.session.add(i9)
        db.session.add(i10)
        db.session.commit()
    except:
        return 'There was an issue adding a tour in dbseed function'

    return 'DATA HAS BEEN LOADED'
