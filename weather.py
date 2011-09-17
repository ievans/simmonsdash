import pywapi

def getWeather(zipcode, pathPrefix = ''):
    weather = pywapi.get_weather_from_google('02139')
    weather['current_conditions']['icon'] = pathPrefix + getIcon(weather['current_conditions']['condition'])
    return weather

def getIcon(condition):
    return '42.png'
