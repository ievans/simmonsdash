import pywapi

def getWeather(zipcode, pathPrefix = ''):
    weather = pywapi.get_weather_from_google('02139')
    weather['current_conditions']['icon'] = parthPrefix + getIcon
    print weather['current_conditions']['icon']
    return weather

def getIcon(condition):
    return '42.png'

print getWeather('02139')
