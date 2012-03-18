from django.http import HttpResponse
import lxml.etree
import json

baseNextBusURL = 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&'

def nextbus(req):
    data = lxml.etree.parse(baseNextBusURL + 'a=mit&r=tech&d=kendsq&s=simmhl')
    next_times = [prediction.get('minutes') for prediction in data.findall('.//predictions/direction/prediction')]
    jsonout = json.dumps(next_times, sort_keys=True, indent=4)
    print jsonout
    return HttpResponse(jsonout, mimetype="application/json")
