import web
from web.contrib.template import render_jinja
from util import fixDates
from settings import DB, TEMPLATES, CHANNEL, GOOGLE_ANALYTICS

urls = (
    '/.*', 'Quotes',
)

class Quotes:
    def GET(self):
        db = web.database(dbn='sqlite', db=DB)
        quotes = db.select('quote', where="channel = '{}'".format(CHANNEL))
        # sort by added date, ascending
        quotes = sorted([fixDates(quote) for quote in quotes], cmp=lambda this, other: cmp(this['datetime'], other['datetime']), reverse=True)
        render = render_jinja(TEMPLATES)
        return render.list(quotes=quotes, channel=CHANNEL, analytics=GOOGLE_ANALYTICS)

if __name__ == '__main__':
    application = web.application(urls, globals())
    application.run()
