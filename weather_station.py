from pyowm import OWM

def weather_station(owm_key, lat, lon):
    owm = OWM(owm_key)
    mgr = owm.weather_manager()

    observation = mgr.weather_at_coords(lat=lat, lon=lon)
    w = observation.weather
    temp = '溫度: ' + str(w.temperature('celsius').get('temp'))
    status = '天氣: ' + w.detailed_status
    humidity = '濕度: ' + str(w.humidity)
    msg = '\n' + status + '\n' + temp + '\n' + humidity + '\n'

    return msg

def main():
    owm_key = '87d4857207c8971a947573aa70fc0210'
    weather = weather_station(owm_key, 23, 121)
    print(weather)

if __name__ == '__main__':
    main()