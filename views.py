from django.http import HttpResponse
from django.shortcuts import render_to_response

#def home(request):
#    return HttpResponse("Hello, world. You're at the poll index.")

def home(req):
    return render_to_response('index.html', { 'date': '1-2-2011' })
