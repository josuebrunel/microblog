from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):

    openid = TextField('openoid', validators = [Required('This fill is required')])
    remember_me = BooleanField('Remember me', default = False)