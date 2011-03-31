from web.contrib.template import render_jinja
import web
import pretty
import datetime

urls = (
    '/.*', 'Quotes',
)

def prettifyDate(quote):
    quote['date'] = pretty.date(datetime.datetime.strptime(quote['date'], "%Y-%m-%d %H:%M:%S"))
    return quote


class Quotes:
    def GET(self):
        db = web.database(dbn='sqlite', db='grouphugs.db')
        quotes = db.select('quote', where="channel = '#grouphugs'")
        quotes = [prettifyDate(quote) for quote in quotes]
        render = render_jinja('templates/')
        return render.list(quotes=quotes)

if __name__ == '__main__':
    #application = web.application(urls, globals()).wsgifunc()
    application = web.application(urls, globals())
    application.run()
