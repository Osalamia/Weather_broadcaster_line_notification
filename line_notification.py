from urllib import response
import requests
import logging

logger = logging.getLogger(__name__)
LINE_URL = 'https://notify-api.line.me/api/notify'

def notify(token, msg):
    headers = {"Authorization": "Bearer " + token, "Content-Type" : "application/x-www-form-urlencoded"}
    payload = {'message': msg}
    response = requests.post(LINE_URL, headers = headers, params = payload)
    return response.status_code


def main():
    line_token = 'lrurcaHLCSYhh7tYokh3WmBaePlR8O2FYnCGRLpJmXq'
    msg = '\n測試'
    status_code = notify(line_token, msg)
    print(status_code)

if __name__ == '__main__':
    logging.basicConfig(
        level = logging.INFO,
        format = '%(asctime)s %(levelname)s %(message)s')
    main()
