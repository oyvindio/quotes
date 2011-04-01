import pretty

import os.path
import datetime

def relativePath(path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)

def addDatetime(quote):
    quote['datetime'] = datetime.datetime.strptime(quote['date'], '%Y-%m-%d %H:%M:%S')
    return quote

def addPrettyDate(quote):
    quote['date_pretty'] = pretty.date(quote['datetime'])
    return quote

def addSimpleDate(quote):
    quote['date_simple'] = quote['datetime'].strftime('%Y%m%d%H%M%S')
    return quote

def fixDates(quote):
    quote = addDatetime(quote)
    quote = addPrettyDate(quote)
    quote = addSimpleDate(quote)
    return quote
