import requests
from datetime import datetime

api_key='067b1fbb40143614cec9e827ed9207ea'
location=input("Enter the name of the city:  ")

comp_api_link= "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link= requests.get(comp_api_link)
api_data=api_link.json()

temp_city=((api_data['main']['temp'])-273.15)
weather_desc=api_data['weather'][0]['description']
hmdt=api_data['main']['humidity']
wind_speed=api_data['wind']['speed']
date_time=datetime.now().strftime("%d %B %Y | %X")

print("\n\n\t-----------   Weather Status Report   -----------")
print("--------------------------------------------------------------------")
print("||Weather stats for --> {}||Time --> {}||".format(location.upper(),date_time))
print("--------------------------------------------------------------------")
print("\n\nCurrent temperature is --> {:.2f} deg C".format(temp_city))
print("Current weather description: ",weather_desc)
print("Humidity at the place: ",hmdt,"%")
print("Current wind speed: ",wind_speed," Kmph")

txtlist=[temp_city,weather_desc,hmdt,wind_speed,date_time]
with open("textfile.txt" , mode = 'w', encoding = 'cp1252') as f:
    f.write("-----------   Weather Status Report   -----------\n")
    f.write("--------------------------------------------------------------------\n")
    f.write("||Weather stats for --> {}||Time --> {}||\n".format(location.upper(),date_time))
    f.write("--------------------------------------------------------------------\n")
    f.write("Current temperature is: {:.2f} deg C\n".format(txtlist[0]))

    f.write("{}{} \n".format("Current weather description  : " ,txtlist[1]))
    f.write("{}{}{} \n".format("Humidity at the place     : ",txtlist[2],"%"))
    f.write("{}{}{} \n".format("Current wind speed    : ",txtlist[3],"kmph"))
