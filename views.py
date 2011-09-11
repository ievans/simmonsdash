from django.http import HttpResponse
from django.shortcuts import render_to_response
from datetime import datetime, timedelta
import calendar
from time import mktime
import pywapi, string

zipcode = "02139"

def home(req):
    return render_to_response('index.html', { 'date': '1-2-2011' })

def events(request):
    import feedparser
    def formatEventsDate(d):
        return d.strftime('%a') if d - datetime.now() < timedelta(7) else d.strftime("%m/%d")
    url = "http://events.mit.edu/rss/index.html?fulltext=&andor=and&categories=24&categories=4&categories=127&categories=2&categories=7&sponsors%3A0=&_rss=Create+RSS+Feed"
    d2 = feedparser.parse(url)
    smallevents = [] # contains only the things we want
    for event in d2['entries']:
        eventDateTime = datetime.fromtimestamp(mktime(event.updated_parsed))
        smallevents.extend([ { 'title' : event['title'],
                               'date' : formatEventsDate(eventDateTime),
                               'time' : eventDateTime.strftime('%I:%M'),
                               'ampm' : eventDateTime.strftime('%p'),
                               'description' : event['description'] } ])

    print smallevents
    return render_to_response('events.html', { 'events' : smallevents })

def calendar(req):
    now = datetime.now()
    return render_to_response('calendar.html', {'monthName' : now.strftime("%B"),
                                                'dayNumber' : now.day,
                                                'clock' : now.strftime("%I:%M"),
                                                'ampm' : now.strftime("%p"),
                                                'dayName' : now.strftime("%A")
                                                })

def weather(req):
    weather = pywapi.get_weather_from_google(zipcode)
    forecasts = weather['forecasts']
    day1 = forecasts[0]
    day2 = forecasts[1]
    
    currentCondition = string.lower(weather['current_conditions']['condition'])
    currentTemp = string.lower(weather['current_conditions']['temp_f'])

    future = []
    for i in range(2):
        future.append((string.lower(forecasts[i]['condition']), string.lower(forecasts[i]['high']), string.lower(forecasts[i]['low'])))
    return render_to_response('weather.html', { 'currentCondition': currentCondition,
                                                'currentTemp':  currentTemp,
                                                'todayCondition': future[0][0],
                                                'todayHigh': future[0][1],
                                                'todayLow': future[0][2],
                                                'nextDayCondition': future[1][0],
                                                'nextDayHigh': future[1][1],
                                                'nextDayLow': future[1][2],
                                                })

