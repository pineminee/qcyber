# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth
import logging

logger = logging.getLogger("web2py.app.qcyber")
logger.setLevel(logging.DEBUG)

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = AppConfig(reload=True)

# db = DAL('mysql://<your_username>:<your_mysql_password>@<your_mysql_hostname>/<your_database_name>')
db = DAL('mysql://atyrysh:qcyberpass@atyrysh.mysql.pythonanywhere-services.com/atyrysh$qcyber', migrate=False)
db.define_table('test', Field('id'), Field('site'))
db.define_table('subreddits', Field('id'), Field('site'))
db.define_table('wiki_articles', Field('id'), Field('site'))
