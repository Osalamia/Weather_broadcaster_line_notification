from line_notification import notify
from weather_station import weather_station

line_token = 'lrurcaHLCSYhh7tYokh3WmBaePlR8O2FYnCGRLpJmXq'
owm_key = '87d4857207c8971a947573aa70fc0210'


def weather_broadcast(line_token, owm_key):
    lat = input('緯度: ')
    lon = input('經度: ')
    msg = weather_station(owm_key, int(lat), int(lon))
    status_code = notify(line_token, msg)
    print(status_code)
    return

if __name__ == '__main__':
    weather_broadcast(line_token, owm_key)