import httpx
from flask import request

WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather';
# API_KEY = '914436bce4832a0cf8d5ab6ed1f5da3d';
API_KEY = '9a94af33a749ba500adf07b62f81e42d';
# end point handler
def get_list(): 
    params = request.args.to_dict()
    # append the api key to query string
    params['appid'] = API_KEY 
    print(params)
    res = httpx.get(WEATHER_API_URL, params=params)
    print(res.url)
    return res.json() 
