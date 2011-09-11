from django.http import HttpResponse
from django.shortcuts import render_to_response

#def home(request):
#    return HttpResponse("Hello, world. You're at the poll index.")

#def home(req):
#    return render_to_response('index.html', { 'date': '1-2-2011' })

def home(request):
    import feedparser
    url = "http://events.mit.edu/rss/index.html?fulltext=&andor=and&categories=24&categories=4&categories=127&categories=2&categories=7&sponsors%3A0=&_rss=Create+RSS+Feed"
    d2 = feedparser.parse(url)
    smallevents = [] # contains only the things we want
    for event in d2['entries']:
        smallevents.extend([ { 'title' : event['title'],
                               'date' : event['date'],
                               'description' : event['description'] } ])

    print smallevents
    return render_to_response('events.html', { 'events' : smallevents })
