import web
from web.contrib.template import render_jinja
from util import addPrettyDate
from settings import DB, TEMPLATES, CHANNEL

urls = (
    '/.*', 'Quotes',
)

class Quotes:
    def GET(self):
        db = web.database(dbn='sqlite', db=DB)
        quotes = db.select('quote', where="channel = '{}'".format(CHANNEL))
        # sort by added date, ascending
        quotes = sorted([addPrettyDate(quote) for quote in quotes], cmp=lambda this, other: cmp(this['datetime'], other['datetime']), reverse=True)
        render = render_jinja(TEMPLATES)
        return render.list(quotes=quotes, channel=CHANNEL)

if __name__ == '__main__':
    application = web.application(urls, globals())
    application.run()
