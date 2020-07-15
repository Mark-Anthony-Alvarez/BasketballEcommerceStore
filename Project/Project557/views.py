from .models import Category, Item, Order
from .forms import CheckoutForm
from . import db
from flask import Blueprint, render_template, url_for, request, session, flash, redirect

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    categories = Category.query.order_by(Category.name).all()
    return render_template('index.html', categories=categories)


@bp.route('/items/<int:categoryid>/')
def categoryitems(categoryid):
    items = Item.query.filter(Item.category_id == categoryid)
    return render_template('categoryitems.html', items=items)


# Referred to as "Cart" to the user
@bp.route('/order', methods=['POST', 'GET'])
def order():
    item_id = request.values.get('item_id')

    if 'order_id' in session.keys():
        order = Order.query.get(session['order_id'])

    else:
        order = None

    if order is None:
        order = Order(status=False, firstname='', surname='',
                      email='', phone='', totalcost=0)
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None

    # Adds total price of 'zero' plus the price of each item that was added to the cart
    totalprice = 0
    if order is not None:
        for item in order.items:
            totalprice = totalprice + item.price

    # Adding two of the same items not permitted

    if item_id is not None and order is not None:
        item = Item.query.get(item_id)
        if item not in order.items:
            try:
                order.items.append(item)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your cart'
            return redirect(url_for('main.order'))
        else:
            flash(
                'We are sorry, there is only one of those items available at this time.')
            return redirect(url_for('main.order'))

    return render_template('order.html', order=order, totalprice=totalprice)


# Delete specific cart items with button on right hand side
@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id = request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        item_to_delete = Item.query.get(id)
        try:
            order.items.remove(item_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))

# Deletes the items from the user's cart


@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('Your cart is now empty.')
    return redirect(url_for('main.index'))


@bp.route('/checkout', methods=['POST', 'GET'])
def checkout():
    form = CheckoutForm()
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])

        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            totalcost = 0
            for item in order.items:
                totalcost = totalcost + item.price
            order.totalcost = totalcost
            try:
                db.session.commit()
                del session['order_id']
                flash(
                    'Your order is on its way! Thank you for your purchase.')
                return redirect(url_for('main.index'))
            except:
                return 'Could not complete order.'
    return render_template('checkout.html', form=form)


@bp.route('/items/')
def search():
    search = request.args.get('search')
    # substrings will match if in the description of the item
    search = '%{}%'.format(search)
    items = Item.query.filter(Item.description.like(search)).all()
    return render_template('categoryitems.html', items=items)
