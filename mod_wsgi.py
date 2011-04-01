import site
import sys
import os.path

prev_sys_path = sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from settings import VIRTUALENV
site.addsitedir(os.path.join(VIRTUALENV, '/lib/python2.7/site-packages'))


new_sys_path = [p for p in sys.path if p not in prev_sys_path]
for item in new_sys_path:
    sys.path.remove(item)
sys.path[:0] = new_sys_path

import web
import quotes
application = web.application(quotes.urls, quotes.__dict__).wsgifunc()
