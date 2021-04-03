from django.shortcuts import render
import json
import datetime
import requests  
#from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def d_t(s):
    return datetime.datetime.fromtimestamp(s).strftime(' %d-%m-%Y %H:%M:%S')

def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=583d7763e0ddee391b4e64335daedc92'
    city=request.POST.get('city')
    data_list=requests.get(url.format(city)).json()
    c_city=city
    if request.method == 'POST' and request.POST.get('city') != '':
        data = {
        'city':c_city,    
        'temperature':str(data_list['main']['temp']) +'°C',
        'country_code':str(data_list['sys']['country']),
        'icon':data_list['weather'][0]['icon'],
        'coordinate':'Latitude : ' + str(data_list['coord']['lon']) + '  Longitude : ' + str(data_list['coord']['lat']),
        'pressure':data_list['main']['pressure'],
        'humidity':data_list['main']['humidity'],
        'clouds':data_list['clouds']['all'],
        'datetime': d_t(int(data_list['dt'])),
        'sunrise':d_t(int(data_list['sys']['sunrise'])),
        'sunset':d_t(int(data_list['sys']['sunset'])),
        'description':data_list['weather'][0]['description'],
        }
    else:
        data = {
        'city':c_city,    
        'temperature':str(data_list['main']['temp']) +'°C',
        'country_code':str(data_list['sys']['country']),
        'icon':data_list['weather'][0]['icon'],
        'coordinate':'Latitude : ' + str(data_list['coord']['lon']) + '  Longitude : ' + str(data_list['coord']['lat']),
        'pressure':data_list['main']['pressure'],
        'humidity':data_list['main']['humidity'],
        'clouds':data_list['clouds']['all'],
        'datetime': d_t(int(data_list['dt'])),
        'sunrise':d_t(int(data_list['sys']['sunrise'])),
        'sunset':d_t(int(data_list['sys']['sunset'])),
        'description':data_list['weather'][0]['description'],
        }
    return render(request,'index.html',data)