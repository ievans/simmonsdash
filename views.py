from django.http import HttpResponse
from django.shortcuts import render_to_response
from datetime import datetime, timedelta
import calendar
from time import mktime
import json
import feedparser
import weather as w
    
zipcode = "02139"
baseUrl = 'http://google.com'

def home(request):
    return render_to_response('index.html', None)

def light(request):
    return render_to_response('light.html', {})

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

def posters(request):
    p={}
    p["posters"]='a.jpg';
    jsonout = json.dumps(p, sort_keys=True, indent=4)
    return HttpResponse(jsonout, mimetype="application/json")

def news(request):
    return extractCalendarEvents('http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&output=rss')

def editorial(request):
    return render_to_response('scroller.html', None)

def extractCalendarEvents(url):
    d2 = feedparser.parse(url)
    smallnews = []
    for newsitem in d2['entries']:
        ts = datetime.fromtimestamp(mktime(newsitem.updated_parsed))
        smallnews.extend([ { 'title' : newsitem['title'],
                             'timestamp' : ts.strftime('%m/%d %I:%M') }])
    jsonout = json.dumps(smallnews, sort_keys=True, indent=4)
    return HttpResponse(jsonout, mimetype="application/json")

def localnews(request):
    return extractCalendarEvents('https://www.google.com/calendar/feeds/simmons-tech%40mit.edu/public/basic')

def weather(request):
    result = w.getWeather('02139', 'media/weather/')
    jsonout = json.dumps(result, sort_keys=True, indent=4)
    return HttpResponse(jsonout, mimetype="application/json")

def editorialList(request):
    import os
    files = os.listdir(os.path.join(os.getcwd(), 'media', 'editorials'))
    files = ['/media/editorials/' + x for x in files]
    jsonout = json.dumps(files, sort_keys=True, indent=4)
    return HttpResponse(jsonout, mimetype="application/json")
