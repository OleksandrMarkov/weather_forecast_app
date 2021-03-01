from pyowm import OWM

# api key from 'https://home.openweathermap.org/api_keys'
token = 'YOUR KEY'

owm = OWM(token)
mgr = owm.weather_manager()

observation = mgr.weather_at_place('Запорожье')

w = observation.weather
wind = observation.weather.wind(unit='miles_hour')   # Default unit: 'meters_sec'

tomorrow = mgr.forecast_at_place('Запорожье', '3h')

print('Status: ' + w.detailed_status)
print('Current temperature (°C): ' + str(w.temperature('celsius')['temp']))
print('Wind`s speed (miles/hour): ' + str(round(wind['speed'], 2)))
print('Humidity: ' + str(w.humidity) + '%')
print('Cloudiness: ' + str(w.clouds) + '%')
print()
print('Is it going to snow tomorrow? ' + str(tomorrow.will_have_snow()))
print('Is it going to fog tomorrow? ' + str(tomorrow.will_have_fog()))