# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import * 
import requests
import json
from datetime import datetime

root= Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("weather app")

city_value= StringVar()

def showWeather():
	api_key = "b428984be1d378e11e54dd82a74335a8"
	city_name = city_value.get()
	weather_url = 'http://api.openweathermap.org/data/2.5/weather?g=' + city_name + '&appid=' + api_key
	response = requests.get(weather_url)
	weather_info = response.json()
	tfield.delete("1.0","end")
	
	if weather_info['cod'] == 200:
		kelvin = 273
		
		temp = int(weather_info['main']['temp'] - kelvin)

		feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
		pressure = weather_info['main']['pressure']
		humidity = weather_info['main']['humidity']
		wind_speed = weather_info['wind']['speed'] * 3.6
		sunrise = weather_info['sys']['sunrise']
		sunset = weather_info['sys']['sunset']
		timezone = weather_info['timezone']
		cloudy = weather_info['clouds']['all']
		description = weather_info['weather'][0]['description']

		sunrise_time = time_format_for_location(sunrise + timezone)
		sunset_time = time_format_for_location(sunset + timezone)

#assigning Values to our weather varaible, to display as output

		weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"

	else:

		weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"



	tfield.insert(INSERT, weather) #to insert or send value in our Text Field to display output
	

#------------------------------Frontend part of code - Interface

city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) #to generate label heading

inp_city = Entry(root, textvariable = city_value, width = 24, font='Arial 14 bold').pack()

Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

#to show output

weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)

tfield = Text(root, width=46, height=10)
tfield.pack()

root.mainloop()