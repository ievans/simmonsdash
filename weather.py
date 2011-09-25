# API for weather. return a python dict with these keys

    ## nowtime - current as of time, eg 12:00 AM
    ## nowicon - url to an image
    ## nowtemp
    ## nowtitle
    ## nowlocation

    ## todayicon
    ## todaytitle
    ## todaytemphigh
    ## todaytemplow

    ## tomorrowicon
    ## tomorrowtitle
    ## tomorrowtemphigh
    ## tomorrowtemplow

import pywapi

def getWeather(zipcode, pathPrefix = ''):
    weather = pywapi.get_weather_from_google('02139')
    weather['current_conditions']['icon'] = pathPrefix + getIcon(weather['current_conditions']['condition'])
    return weather

def getIcon(condition):
    return '42.

