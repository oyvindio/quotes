import web
from web.contrib.template import render_jinja
from util import fixDates
from settings import DB, TEMPLATES, CHANNEL, GOOGLE_ANALYTICS

urls = (
    '/.*', 'Quotes',
)

class Quotes(object):
    def GET(self):
        db = web.database(dbn='sqlite', db=DB)
        quotes = db.select('quote', where="channel = '{}'".format(CHANNEL), order='date desc')
        quotes = [fixDates(quote) for quote in quotes]
        render = render_jinja(TEMPLATES)
        return render.list(quotes=quotes, channel=CHANNEL, analytics=GOOGLE_ANALYTICS)

if __name__ == '__main__':
    application = web.application(urls, globals())
    application.run()
