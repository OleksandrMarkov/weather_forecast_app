from tkinter import *

import requests

from tkinter import messagebox


window = Tk()

def get_weather():

	city = city_field.get()
 
	# openweathermap.org
	key = '7256f983dffe39f8d1a1094d221a30e0'

	url = 'http://api.openweathermap.org/data/2.5/weather'

	params = {'APPID': key, 'q': city, 'units': 'metric'}

	try:
		result = requests.get(url, params=params)

		weather = result.json()

		info['text'] = f'{str(weather["name"])}: {str(weather["main"]["temp"])} °C'
	except:	
		messagebox.showinfo( 'Try again!','Wrong city!')
		city_field.delete(0, END) # clearing 

window['bg'] = '#dcdcdc'

window.title('Weather app')

window.geometry('300x250')
window.resizable(width=False, height=False)

frame_top = Frame(window, bg='#FCCF5B', bd=5)
# position
frame_top.place(relx=0.15,relwidth=0.75, relheight=0.55)
#relx=0.15, rely=0.15, 

frame_bottom = Frame(window, bg='#FCCF5B', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.75, relheight=0.45)
#

city_field = Entry(frame_top, bg='white', font="Arial 24")
city_field.pack()


get_temp_btn = Button(frame_top, font="Arial 14", text='find out it!', bg = '#C2FAFF', activebackground = '#F95C85', bd = 3, command=get_weather)
get_temp_btn.pack()


info = Label(frame_bottom, bg='#FCCF5B', font=40)
info.pack()


window.mainloop()