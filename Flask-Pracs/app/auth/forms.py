from flask_wtf import Form
from wtforms import (
StringField, 
TextAreaField, 
PasswordField, 
IntegerField, 
RadioField, 
SelectField,
SubmitField,
validators
) 

GENDER =[('Male','M'),('Female','F')]

# Register Form Class
class RegisterForm(Form):
    """ Registerform for registering users """
    name = StringField('*Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('*Email', [validators.Length(min=6, max=50)])
    password = PasswordField('*Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('*Confirm Password',[validators.DataRequired()])
    address = TextAreaField('Address', [validators.optional(), validators.length(max=200)])

class ProfileEditForm(Form):
    """ PrfoileEditform for editing users profile """
    username = StringField("Username",[validators.DataRequired()])
    email = StringField("Email",[validators.DataRequired(), validators.Length(1,64),validators.Email()])
    contact = IntegerField("Contact",[validators.optional()])
    address = TextAreaField("Address")
    gender = SelectField("Gender",choices=GENDER)
    submit= SubmitField("Save Profile")
