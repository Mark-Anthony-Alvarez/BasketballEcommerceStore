from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email

# form that will be used after clicking checkout from the order page.


class CheckoutForm(FlaskForm):
    firstname = StringField("First Name: ", validators=[InputRequired()])
    surname = StringField("Last Name: ", validators=[InputRequired()])
    address = StringField("Shipping Address: ",
                          validators=[InputRequired()])
    email = StringField("E-mail Address: ",
                        validators=[InputRequired(), email()])
    phone = StringField("Phone Number: ", validators=[InputRequired()])

    submit = SubmitField("-Place Your Order-")
