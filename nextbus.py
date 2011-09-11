from django.shortcuts import render_to_response
import lxml.etree

baseNextBusURL = 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&'

def nextbus(req):
    data = lxml.etree.parse(baseNextBusURL + 'a=mbta&r=1&d=1_1_var0&s=731&ts=74')
    next_times = [prediction.get('minutes') for prediction in data.findall('.//predictions/direction/prediction')]
    return render_to_response('nextbus.html', {'times': next_times})

