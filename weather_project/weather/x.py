from django.shortcuts import render
import requests
import datetime

def d_t(s):
    return datetime.datetime.fromtimestamp(s).strftime(' %Y-%m-%d %H:%M:%S')

url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=583d7763e0ddee391b4e64335daedc92'
city='Mumbai'

data_list=requests.get(url.format(city)).json()
data = {
        'temperature':str(data_list['main']['temp']) +'°C',
        'country_code':data_list['sys']['country'],
        'coordinate':'Latitude : ' + str(data_list['coord']['lon']) + '  Longitude : ' + str(data_list['coord']['lat']),
        'pressure':data_list['main']['pressure'],
        'humidity':data_list['main']['humidity'],
        'clouds':data_list['clouds']['all'],
        'datetime': d_t(int(data_list['dt'])),
        'sunrise':d_t(int(data_list['sys']['sunrise'])),
        'sunset':d_t(int(data_list['sys']['sunset'])),
        'icon':data_list['weather'][0]['icon'],
        'description':data_list['weather'][0]['description'],
}
print(data)
