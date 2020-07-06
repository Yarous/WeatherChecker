from pyowm import OWM
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style

owm = OWM('8ec1b98a13b3ac75851647f831eecd90', language = "en")  

place = input("Please enter you city: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()
temp = w.get_temperature('celsius')["temp"]

print( Back.GREEN )
print("In city " + place + w.get_detailed_status())

print( Back.RED )
print("Temperature now: " + str(temp))

if temp < 10:
	print( Back.BLUE )
	print("Now PPC how cold, dress like a tank!")
elif temp < 20:
	print( Back.BLUE )
	print("It's cold, get dressed warmer!")
else:
	print( Back.YELOW )
	print("The temperature is good, wear whatever you want!")
