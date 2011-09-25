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
    result = {}
    result['nowtime'] = weather['forecast_information']['current_date_time']
    result['nowicon'] = pathPrefix + getIcon(weather['current_conditions']['condition'])
    result['nowtemp'] = weather['current_conditions']['temp_f']
    result['nowtitle'] = weather['current_conditions']['condition']
    result['nowlocation'] = weather['forecast_information']['city']
    
    result['todayicon'] = pathPrefix + getIcon(weather['forecasts'][0]['condition']) 
    result['todaytitle'] = weather['forecasts'][0]['condition']
    result['todaytemphigh'] = weather['forecasts'][0]['high']
    result['todaytemplow'] = weather['forecasts'][0]['low']

    result['tomorrowicon'] = pathPrefix + getIcon(weather['forecasts'][1]['condition'])
    result['tomorrowtitle'] = weather['forecasts'][1]['condition']
    result['tomorrowtemphigh'] = weather['forecasts'][1]['high']
    result['tomorrowtemplow'] = weather['forecasts'][1]['low']
    
    return result

def getIcon(condition):
    c2icon = {'Clear': '32', 
              'Cloudy': '23', 
              'Fog': '20',
              'Haze': '19',
              'Light Rain': '11',
              'Mostly Cloudy': '28',
              'Overcast': '26',
              'Partly Cloudy': '30',
              'Rain': '11',
              'Rain Showers': '10',
              'Showers': '8',
              'Thunderstorm': '4',
              'Chance of Showers': '8',
              'Chance of Snow': '15',
              'Chance of Storm': '3',
              'Mostly Sunny': '32',
              'Partly Sunny': '44',
              'Scattered Showers': '1',
              'Sunny': '36'}

    return c2icon[condition] + '.png'
