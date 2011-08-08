from __future__ import division
import math
import web
from web.contrib.template import render_jinja
from util import fixDates
from settings import DB, TEMPLATES, CHANNEL, GOOGLE_ANALYTICS, PER_PAGE

urls = (
    '/.*', 'Quotes',
)

class Quotes(object):
    def GET(self):
        params = web.input()
        page = int(params.p) if hasattr(params, 'p') else 1
        offset = (page - 1) * PER_PAGE
        db = web.database(dbn='sqlite', db=DB)
        quote_count = db.query("select count(*) as count from quote where channel='{}'".format(CHANNEL))[0].count
        quotes = db.select('quote', where="channel = '{}'".format(CHANNEL),
                           order='date desc', limit='$l', offset='$o',
                           vars={'l': PER_PAGE, 'o': offset})
        quotes = [fixDates(quote) for quote in quotes]
        pages = int(math.ceil(quote_count / PER_PAGE))
        render = render_jinja(TEMPLATES)
        return render.list(quotes=quotes, channel=CHANNEL,
                           analytics=GOOGLE_ANALYTICS, page=page, pages=pages)

if __name__ == '__main__':
    application = web.application(urls, globals())
    application.run()

