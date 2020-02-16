import tkinter as tk
import requests
from tkinter import font

def test_function(entry):
    print('Button clicked! ', entry)

def formatting(weather):
    try:
        city=weather['name']
        description=weather['weather'][0]['description']
        tempreture=weather['main']['temp']

        result= str(city) + '\n ' + str(description) + '\n '+ str(tempreture)
    except:
        result = 'Error in accessing that information'

    return result


def get_weather(sl): 
    key= '83deace47af180a3f5d2cefb1ba96153'
    url= 'https://api.openweathermap.org/data/2.5/weather'
    param= {'APPID': key, 'q':sl, 'units':'Imperial'} #request from server
    response= requests.get(url,params=param)
    weather=response.json()

    label['text']= formatting(weather)
    

    print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
#api.openweathermap.org/data/2.5/weather?q={city name} current weather
#83deace47af180a3f5d2cefb1ba96153  API

root = tk.Tk()

canvas=tk.Canvas(root,height=500,width=800)
canvas.pack()

background_image=tk.PhotoImage(file='Interlocking-UH-Beveled-White-Gray.gif')
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

frame=tk.Frame(root, bg='#ff4d4d', bd=5)
frame.place(relx=0.6,rely=0.1, relwidth=0.39,relheight=0.1)

entry=tk.Entry(frame)
entry.place(relx=0,rely=0,relwidth=0.5,relheight=1)

button= tk.Button(frame,text='Get Weather',bg='gray',command=lambda:get_weather(entry.get())) #lamda works at run, temp. stored in memory
button.place(relx=0.6,rely=0,relwidth=0.4,relheight=1)

lower_frame=tk.Frame(root,bg='#ff4d4d', bd=5)
lower_frame.place(relx=0.6, rely=0.3,relwidth=0.39,relheight=0.5)


label=tk.Label(lower_frame, font=('Courier', 18),anchor='nw', justify='left', bd=4)
label.place(relwidth=1,relheight=1)






root.mainloop()
