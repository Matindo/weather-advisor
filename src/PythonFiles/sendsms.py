#!/usr/bin/env python3
from sqldb import *

# Download the helper library from https://www.twilio.com/docs/python/install
import requests
import emoji
from twilio.rest import Client
from datetime import datetime

# Your Account SID from twilio.com/console
account_sid = "ACb2b6975e7e22138bebc6a586ea1fdaf9"

# Your Auth Token from twilio.com/console
auth_token = "ba5affb9dfbbab815c259705bf209af0"

client = Client(account_sid, auth_token)
def sendMessage(fr,to,body):
    message = client.messages.create(
         body=body,
         from_=fr,
         to=to
     )
    print(message.status)   


#Arrays to store various codes from OWM to use emojis
thunder = [200,201,202,210,211,212,221,230,231,232] #cloud_with_lightning_and_rain
drizzle = [300,301,302,311,312,313,314,321] #cloud_with_rain
light_rain=[500,501,520] #sun_behind_rain_cloud
heavy_rain=[502,503,504,521,522,531] #umbrella_with_rain_drops
snow=[600,601,602,611,612,613,620,621,622] #snowflake
rain_and_snow=[615,616] #cloud_with_snow
mist = [701,711,721,731,741,751,761,762,771] #fog
tornado=[781] #tornado
clear = [800] #Depends on time of day. Daytime sun. Nighttime =full_moon
cloudy = [801,802,803,804] #Depend on time of day. Daytime= sun_behind_cloud. Nighttime = cloud

# Function to build the string for the text
def text_func(fName, lName, city, humidity, wind, description, temp, emoticon):
    text = [f'\nHello {fName} {lName}\n' +'City: ',str(city), '\nDescription: ', str(description),'\t',emoticon, '\nTemperature: ', str(temp),'°C\n', 'Wind: ', str(wind), 'km/h', '\nHumidity: ', str(humidity), "%"]
    return text

# Function to match and emoji to the respective id using UTF-8 encoding
def map_emojis(id):
    if (id in thunder ):
        emoticon=emoji.emojize(':cloud_with_lightning_and_rain:')
    elif (id in drizzle):
        emoticon=emoji.emojize(':cloud_with_rain:')
    elif (id in light_rain):
        emoticon=emoji.emojize(':cloud_with_lightning_and_rain:')
    elif (id in heavy_rain):
        emoticon=emoji.emojize(':umbrella_with_rain_drops:')
    elif (id in snow):
        emoticon=emoji.emojize(':snowflake:')
    elif (id in rain_and_snow):
        emoticon=emoji.emojize(':cloud_with_snow:')
    elif (id in mist):
        emoticon=emoji.emojize(':fog:')
    elif (id in tornado):
        emoticon=emoji.emojize(':tornado:')
    elif (id in clear):
        if (datetime.now().hour > 19):
            emoticon=emoji.emojize(':full_moon:')
        else:
            emoticon=emoji.emojize(':sun:')
    elif (id in cloudy):
        if (datetime.now().hour > 19):
            emoticon=emoji.emojize(':cloud:')
        else:
            emoticon=emoji.emojize(':sun_behind_cloud:')
    else:
        emoticon=None
    return emoticon

# Main function to send data to each user
if reg_users:
    for user in reg_users:
        # Send to each user with their configured data
        fName = user[0]
        lName = user[1]
        phone = user[3]
        city = user[4]

        if 'lon' in city:
            city_arr = city.split(":")
            lon= city_arr[1].split(",")[0]
            lat= city_arr[2].split("}")[0]
            weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid=b2e0c800233938ec24c6799a64503973'.format(lat,lon)
        else:
            weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b2e0c800233938ec24c6799a64503973&units=metric'.format(city)

        # Weather url is for daily while forecast_url is for 4-day forecast
        # weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b2e0c800233938ec24c6799a64503973&units=metric'.format(city)
        # forecast_url= 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid=b2e0c800233938ec24c6799a64503973&units=metric'.format(city)

        res = requests.get(weather_url)
        data = res.json()
        #print(data)

        try: 
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind = data['wind']['speed']
            description = data['weather'][0]['description']
            id = data['weather'][0]['id']
            temp = data['main']['temp']
            city = data['name']

        except:
            #print("Error with City name or data")
            exit(0)
        
        # Mapping emojis to array
        emoticon = map_emojis(id)


        text = text_func(fName, lName, city, humidity, wind, description, temp, emoticon)

        text= ''.join(text)
        # print(text)
        # sendMessage('+19498066165', phone , text)

if farmers:
    for user in farmers:
        # Send to each user with their configured data
        fName = user[0]
        lName = user[1]
        phone = user[3]
        city = user[4]

        if 'lon' in city:
            city_arr = city.split(":")
            lon=city_arr[1].split(",")[0]
            lat=city_arr[2].split("}")[0]
            weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid=b2e0c800233938ec24c6799a64503973'.format(lat,lon)
        else:
            weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b2e0c800233938ec24c6799a64503973&units=metric'.format(city)

        # Weather url is for daily while forecast_url is for 4-day forecast
        # forecast_url= 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid=b2e0c800233938ec24c6799a64503973&units=metric'.format(city)

        res = requests.get(weather_url)
        data = res.json()
        #print(data)

        try: 
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind = data['wind']['speed']
            description = data['weather'][0]['description']
            id = data['weather'][0]['id']
            temp = data['main']['temp']
            city = data['name']

        except:
            #print("Error with City name or data")
            exit(0)
        
        # Mapping emojis to array
        emoticon = map_emojis(id)

        text = text_func(fName, lName, city, humidity, wind, description, temp, emoticon)

        text= ''.join(text)
        sendMessage('+19498066165', phone , text)

if org:
    for user in org:
        # Send to each user with their configured data
        oname = user[0]
        phone = user[2]
        city = user[3] 


        if 'lon' in city:
            city_arr = city.split(":")
            lon=city_arr[1].split(",")[0]
            lat=city_arr[2].split("}")[0]
            weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid=b2e0c800233938ec24c6799a64503973'.format(lat,lon)
        else:
            weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b2e0c800233938ec24c6799a64503973&units=metric'.format(city)

        # Weather url is for daily while forecast_url is for 4-day forecast
        # forecast_url= 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid=b2e0c800233938ec24c6799a64503973&units=metric'.format(city)
        
        res = requests.get(weather_url)
        data = res.json()
        # print(data)

        try: 
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind = data['wind']['speed']
            description = data['weather'][0]['description']
            id = data['weather'][0]['id']
            temp = data['main']['temp']
            city = data['name']

        except:
            #print("Error with City name or data")
            exit(0)
        
        # Mapping emojis to array
        emoticon = map_emojis(id)

        text = f'\nHello,   {oname}\n' +'City: ',str(city), '\nDescription: ', str(description),'\t',emoticon, '\nTemperature: ', str(temp),'°C\n', 'Wind: ', str(wind), 'km/h', '\nHumidity: ', str(humidity), "%"

        text= ''.join(text)
        print(text)
        # sendMessage('+19498066165', phone , text)







