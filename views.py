from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
import calendar

#def home(request):
#    return HttpResponse("Hello, world. You're at the poll index.")

def home(req):
    return render_to_response('index.html', { 'date': '1-2-2011' })

def calendar(req):
    now = datetime.datetime.now()
    return render_to_response('calendar.html', {'monthName' : now.strftime("%B"),
                                                'dayNumber' : now.day,
                                                'clock' : now.strftime("%I:%M"),
                                                'ampm' : now.strftime("%p"),
                                                'dayName' : now.strftime("%A")
                                                })
