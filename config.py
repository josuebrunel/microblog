import os
from email_secret import MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD

basedir = os.path.abspath(os.path.dirname(__file__))

CSFR_ENABLED = True
SECRET_KEY = '13ru11el120u12a'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }
]

#DATABASE
SQLALCHEMY_DATABASE_URI = "mysql://flask:flask@localhost/microbloging"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')

#ADMINS
ADMINS = [
    'josue@josuebrunel',
]

POSTS_PER_PAGE = 3