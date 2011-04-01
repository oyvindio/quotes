import web
from web.contrib.template import render_jinja
from util import relativePath, addPrettyDate

DB = relativePath('grouphugs.db')
TEMPLATES = relativePath('templates/')

urls = (
    '/.*', 'Quotes',
)

class Quotes:
    def GET(self):
        db = web.database(dbn='sqlite', db=DB)
        quotes = db.select('quote', where="channel = '#grouphugs'")
        # sort by added date, ascending
        quotes = sorted([addPrettyDate(quote) for quote in quotes], cmp=lambda this, other: cmp(this['datetime'], other['datetime']), reverse=True)
        render = render_jinja(TEMPLATES)
        return render.list(quotes=quotes)

if __name__ == '__main__':
    application = web.application(urls, globals())
    application.run()
