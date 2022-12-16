#!/usr/bin/env python3
import requests
from sqldb import *
import matplotlib.pyplot as plt


# Function to build the string for the text
def text_func(fName, lName, city, humidity, wind, description, temp, ):
    text = [f'\nHello, {fName} {lName}\n' +'City: ',str(city), '\nDescription: ', str(description),'\t', '\nTemperature: ', str(temp),'°C\n', 'Wind: ', str(wind), 'km/h', '\nHumidity: ', str(humidity), "%"]
    return text

# Main function to send data to each user
if reg_users:
    for user in reg_users:
        # Send to each user with their configured data
        fName = user[0]
        lName = user[1]
        email = user[2]
        phone = user[3]
        city = user[4]
        tel_true = user[5]


        if 'lon' in city:
                city_arr = city.split(":")
                lon=city_arr[1].split(",")[i]
                lat=city_arr[2].split("}")[i]
                weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid=b2e0c800233938ec24c6799a64503973'.format(lat,lon)
        else:
            weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b2e0c800233938ec24c6799a64503973&units=metric'.format(city)

        # Weather url is for daily while forecast_url is for 4-day forecast
        # forecast_url= 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid=b2e0c800233938ec24c6799a64503973&units=metric'.format(city)
            
        res = requests.get(weather_url)
        data = res.json()

        try: 
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind = data['wind']['speed']
            description = data['weather'][0]['description']
            #id = data['weather'][i]['id']
            temp = data['main']['temp']
        except:
            #print("Error with City name or data")
            exit(0)

        message = text_func(fName, lName, city, humidity, wind, description, temp)
        message= ''.join(message)

        import win32com.client
        ol=win32com.client.Dispatch("outlook.application")
        olmailitem=0x0 #size of the new email
        newmail=ol.CreateItem(olmailitem)
        newmail.Subject= 'Misimu Weather Forecast'
        newmail.To=email
        #newmail.CC='xyz@gmail.com'
        newmail.Body= message
        # attach='C:\\Users\\admin\\Desktop\\Python\\Sample.xlsx'
        # newmail.Attachments.Add(attach)
        # To display the mail before sending it
        # newmail.Display() 
        # newmail.Send()

if farmers:
    for user in farmers:
        # Send to each user with their configured data
        fName = user[0]
        lName = user[1]
        email = user[2]
        phone = user[3]
        city = user[4]

 
        if 'lon' in city:
                city_arr = city.split(":")
                lon=city_arr[1].split(",")[i]
                lat=city_arr[2].split("}")[i]
                weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid=b2e0c800233938ec24c6799a64503973'.format(lat,lon)
                forecast_url= 'http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&units=metric&appid=b2e0c800233938ec24c6799a64503973&units=metric'.format(city)
        else:
            weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b2e0c800233938ec24c6799a64503973&units=metric'.format(city)
            forecast_url= 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid=b2e0c800233938ec24c6799a64503973&units=metric'.format(city)

        # Weather url is for daily while forecast_url is for 4-day forecast
        # forecast_url= 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid=b2e0c800233938ec24c6799a64503973&units=metric'.format(city)
            
        res = requests.get(forecast_url)
        data = res.json()
        all_data_arr= []
        temp_data = []
        rainfall_data = []
        humidity_data = []
        windspeed_data = []

        for i in range(40):
            humidity = data['list'][i]['main']['humidity']
            pressure = data['list'][i]['main']['pressure']
            wind = data['list'][i]['wind']['speed']
            description = data['list'][i]['weather'][0]['description']
            temp = data['list'][i]['main']['temp']
            rainfall = data['list'][i]['pop']
            temp_data.append((i+1,temp))
            rainfall_data.append((i+1,rainfall))
            humidity_data.append((i+1,humidity))
            windspeed_data.append((i+1,wind))
        
        # Create a figure with two subplots
        fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=4, figsize=(20, 20))
        
        # Plot the data for the first graph
        ax1.plot(*zip(*temp_data), label='Temperature')
        ax1.legend()
        ax1.set_title('Temperature Forecast')
        ax1.set_xlabel('Day')
        ax1.set_ylabel('Temperature')

        # Plot the data for the first graph
        ax2.plot(*zip(*rainfall_data), label='Rainfall')
        ax2.legend()
        ax2.set_title('Rainfall Forecast')
        ax2.set_xlabel('Day')
        ax2.set_ylabel('Rainfall')

        # Plot the data for the first graph
        ax3.plot(*zip(*humidity_data), label='Humidity')
        ax3.legend()
        ax3.set_title('Humidity Forecast')
        ax3.set_xlabel('Day')
        ax3.set_ylabel('Humidity')

        # Plot the data for the first graph
        ax4.plot(*zip(*windspeed_data), label='Wind Speed')
        ax4.legend()
        ax4.set_title('Wind Forecast')
        ax4.set_xlabel('Day')
        ax4.set_ylabel('Wind Speed')
        
        # Save the figure to a PDF file
        fig.savefig('farmerdata.pdf')

            # arr_data = [description,temp,wind,pressure,rainfall,humidity]
            # all_data_arr.append(arr_data)
        
        message = text_func(fName, lName, city, humidity, wind, description, temp)

        message= ''.join(message)

        import win32com.client
        ol=win32com.client.Dispatch("outlook.application")
        olmailitem=0x0 #size of the new email
        newmail=ol.CreateItem(olmailitem)
        newmail.Subject= 'Misimu Weather Forecast'
        newmail.To=email
        #newmail.CC='xyz@gmail.com'
        newmail.Body= message
        attach='C:\\Users\\user\\OneDrive\\Desktop\\Drive D\\D\\SchoolWork\\3.2\\Commercial Programming\\Project\\message-apis\\farmerdata.pdf'
       
        newmail.Attachments.Add(attach)
        # To display the mail before sending it
        # newmail.Display() 
        newmail.Send()

        
if org:
    for user in org:
        # Send to each user with their configured data
        oname = user[0]
        email = user[1]
        city = user[3] 
        # tel_true = user[4]

        if 'lon' in city:
                city_arr = city.split(":")
                lon=city_arr[1].split(",")[i]
                lat=city_arr[2].split("}")[i]
                weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid=b2e0c800233938ec24c6799a64503973'.format(lat,lon)
        else:
            weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b2e0c800233938ec24c6799a64503973&units=metric'.format(city)

        # Weather url is for daily while forecast_url is for 4-day forecast
        # forecast_url= 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid=b2e0c800233938ec24c6799a64503973&units=metric'.format(city)
            
        res = requests.get(weather_url)
        data = res.json()

        try: 
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind = data['wind']['speed']
            description = data['weather'][i]['description']
            #id = data['weather'][i]['id']
            temp = data['main']['temp']
        except:
            #print("Error with City name or data")
            exit(0)

        message = f'\nHello,{oname}\n' +'City: ',str(city), '\nDescription: ', str(description),'\t', '\nTemperature: ', str(temp),'°C\n', 'Wind: ', str(wind), 'km/h', '\nHumidity: ', str(humidity), "%"

        message= ''.join(message)

        import win32com.client
        ol=win32com.client.Dispatch("outlook.application")
        olmailitem=0x0 #size of the new email
        newmail=ol.CreateItem(olmailitem)
        newmail.Subject= 'Misimu Weather Forecast'
        newmail.To=email
        #newmail.CC='xyz@gmail.com'
        newmail.Body= message
        # attach='C:\\Users\\admin\\Desktop\\Python\\Sample.xlsx'
        # newmail.Attachments.Add(attach)
        # To display the mail before sending it
        # newmail.Display() 
        newmail.Send()
        # print(message)