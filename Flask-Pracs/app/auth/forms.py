from wtforms import Form, StringField, TextAreaField, PasswordField, IntegerField, RadioField, validators

# Register Form Class
class RegisterForm(Form):
    name = StringField('*Name', [validators.Length(min=1, max=50)])
    username = StringField('*Username', [validators.Length(min=4, max=25)])
    email = StringField('*Email', [validators.Length(min=6, max=50)])
    password = PasswordField('*Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('*Confirm Password',[validators.DataRequired()])
    address = TextAreaField('Address', [validators.optional(), validators.length(max=200)])
    contact = IntegerField('Contact', [validators.optional()])
    gender = RadioField('Gender', [validators.optional()], choices=[('value','Male'),('value_two','Female')])


