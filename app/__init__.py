import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail

from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask.ext.babel import Babel

from config import basedir
from config import ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD, MAIL_PORT, MAIL_SSL

from momentsjs import Momentsjs

    
app = Flask(__name__)
app.config.from_object('config')

app.jinja_env.globals['momentjs'] = Momentsjs #We expose that call as a global variable for all templates

babel = Babel(app)

##LOGGING INTO EMAIL
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@'+MAIL_SERVER, ADMINS, 'microblog failure', credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
##

##LOGGING INTO FILE
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')
##

#Email
mail = Mail(app)
    
#Init DB
db = SQLAlchemy(app)
try:
    db.create_all()
except Exception, e:
    print(e)
    
#Login Manager
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login' #Tells LoginManager what is the login view

#OpenID
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views