WTF_CSRF_ENABLED = True
SECRET_KEY = '******************************'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

MAIL_SERVER='smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = '**********'
MAIL_PASSWORD = '**********'
MAIL_USE_TLS = False
MAIL_USE_SSL = True

ADMINS = ['***********@gmail.com']
