import site
import sys
import os.path

# add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# must be imported *after* project root is added to sys.path
from settings import VIRTUALENV

#add virtualenv site-packages to environment
site.addsitedir(os.path.join(VIRTUALENV, '/lib/python2.7/site-packages'))

# must be imported *after* virtualenv site-packages is added to the environment
import web
import quotes
# bootstrap the wsgi app
application = web.application(quotes.urls, quotes.__dict__).wsgifunc()
