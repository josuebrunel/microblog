from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length

class LoginForm(Form):

    openid = TextField('openoid', validators = [Required('This field is required')])
    remember_me = BooleanField('Remember me', default = False)

class EditForm(Form):
    nickname = TextField('nickname', validators = [Required('Please fill this field')])
    about_me = TextAreaField('about_me', validators = [Length(min=0, max=140)])
    