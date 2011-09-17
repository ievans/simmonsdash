from django.http import HttpResponse
from django.shortcuts import render_to_response
from datetime import datetime, timedelta
import calendar
from time import mktime
import pywapi, string
import json
import feedparser
    
zipcode = "02139"
baseUrl = 'http://google.com'

def home(request):
    return render_to_response('index.html', { 'date': '1-2-2011' })

def events(request):
    def formatEventsDate(d):
        st = d.strftime('%a') if d - datetime.now() < timedelta(7) else d.strftime("%m/%d")
        shorttime = eventDateTime.strftime('%I:%M')
        if shorttime[0] == '0': shorttime = shorttime[1:]
        if shorttime[-3:] == ':00': shorttime = shorttime[:-3]
        st += ' ' + shorttime + eventDateTime.strftime('%p')[0].lower()
        return st
    
    url = "http://events.mit.edu/rss/index.html?fulltext=&andor=and&categories=24&categories=4&categories=127&categories=2&categories=7&sponsors%3A0=&_rss=Create+RSS+Feed"
    d2 = feedparser.parse(url)
    smallevents = [] # contains only the things we want
    for event in d2['entries']:
        eventDateTime = datetime.fromtimestamp(mktime(event.updated_parsed))
        smallevents.extend([ { 'title' : event['title'],
                               'timestamp' : formatEventsDate(eventDateTime),
                               'eventdescription' : event['description'] } ])
    jsonout = json.dumps(smallevents, sort_keys=True, indent=4)
    return HttpResponse(jsonout, mimetype="application/json")

def calendar(request):
    now = datetime.now()
    calender = {'month' : now.strftime("%B"),
     'day' : now.day,
     'clock' : now.strftime("%I:%M:%S") + ' ' + now.strftime("%p"),
     'dayofweek' : now.strftime("%A")
     }
    jsonout = json.dumps(calender, sort_keys=True, indent=4)
    return HttpResponse(jsonout, mimetype="application/json")

def news(request):
    url = 'http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&output=rss'
    d2 = feedparser.parse(url)
    smallnews = []
    for newsitem in d2['entries']:
        ts = datetime.fromtimestamp(mktime(newsitem.updated_parsed))
        smallnews.extend([ { 'title' : newsitem['title'],
                             'timestamp' : ts.strftime('%m/%d %I:%M') }])
    jsonout = json.dumps(smallnews, sort_keys=True, indent=4)
    return HttpResponse(jsonout, mimetype="application/json")

def weather(request):
    weather = pywapi.get_weather_from_google(zipcode)
    forecasts = weather['forecasts']
    day1 = forecasts[0]
    day2 = forecasts[1]
    
    currentCondition = string.lower(weather['current_conditions']['condition'])
    currentTemp = string.lower(weather['current_conditions']['temp_f'])
    currentIconURL = baseUrl + string.lower(weather['current_conditions']['icon'])

    future = []
    for i in range(2):
        future.append((string.lower(forecasts[i]['condition']), string.lower(forecasts[i]['high']), string.lower(forecasts[i]['low'])))
    return render_to_response('weather.html', { 'currentCondition': currentCondition,
                                                'currentTemp': currentTemp,
                                                'currentIcon': currentIconURL,
                                                'todayCondition': future[0][0],
                                                'todayHigh': future[0][1],
                                                'todayLow': future[0][2],
                                                'nextDayCondition': future[1][0],
                                                'nextDayHigh': future[1][1],
                                                'nextDayLow': future[1][2],
                                                })

