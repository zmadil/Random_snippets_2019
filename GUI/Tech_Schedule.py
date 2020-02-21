import tkinter as tk
import requests
from tkinter import font
from tkinter import messagebox
import random
import sqlite3


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


root = tk.Tk()
root.geometry('700x550')
root.title('Tech Floor Assignment')
root.resizable(width=False, height=False)



background_image=tk.PhotoImage(file='CheckList.png')
background_label=tk.Label(root,image=background_image)
background_label.place(relx=0,rely=0,relwidth=1,relheight=0.5)

frame=tk.Frame(root, bd=2)
frame.place(relx=0.52,rely=0.5,relwidth=0.48,relheight=0.1)

entry=tk.Entry(frame)
entry.insert(0,'Sugar Land')
entry.place(relx=0,rely=0.1,relwidth=0.5,relheight=0.5)

button= tk.Button(frame,text='Get weather',command=lambda:get_weather(entry.get())) #lamda works at run, temp. stored in memory
button.place(relx=0.52,rely=0.05,relwidth=0.3,relheight=0.5)

lower_frame=tk.Frame(root,bd=1)
lower_frame.place (relx=0.52,rely=0.6,relwidth=0.48,relheight=0.4)


label=tk.Label(lower_frame, font=('Courier', 12),anchor='nw', bd=40)
label.place(relwidth=1,relheight=1)

###########################xcbcvbvcbxcv cxv

left_frame=tk.Frame(root, bd=8)
left_frame.place(relx=0, rely=0.5,relwidth=0.5,relheight=0.5)





def ApplytoLabel():
    get_size=size.get()
    if get_size==2:
        floors=['1st and BH', '2nd and 3rd']
        random.shuffle(floors)
        for i in range(get_size):
            element = box_list[i].get() # Get value from corresponding Entry
            ArrayLabel=tk.Label(left_frame,text='The Tech ' +element +' will have ' +floors[i] )
            ArrayLabel.pack()
    elif get_size==3:
        floors=['1st and BH', '2nd','3rd']
        random.shuffle(floors)
        for i in range(get_size):
            element = box_list[i].get() # Get value from corresponding Entry
            ArrayLabel=tk.Label(left_frame,text='The Tech ' +element +' will have ' + floors[i])
            ArrayLabel.pack()
    elif get_size == 4:
        floors=['1st', '2nd', '3rd','BH']
        random.shuffle(floors)
        for i in range(get_size):
            element = box_list[i].get() # Get value from corresponding Entry
            ArrayLabel=tk.Label(left_frame,text='The Tech ' +element +' will have ' + floors[i])
            ArrayLabel.pack()
    else:
        ArrayLabel=tk.Label(left_frame,text='Not Possible')
        ArrayLabel.pack()

    


# Create list of Entrys
box_list = []   
floors=[]
def Boxes():
    get_size=size.get()
    for i in range(get_size):        
        box=tk.Entry(left_frame)
        box.pack()
        box_list.append(box)    # Append current Entry to list
    ApplytoLabel1=tk.Button(left_frame,text="Proceed",command=ApplytoLabel)
    ApplytoLabel1.pack()

#Bottom Half Frame


Array = tk.Frame(left_frame)
Array.pack()

text1=tk.Label(Array,text="Techs working : ",
               font="Arial 12")
text1.grid(row=5,column=0)

size=tk.IntVar()

ArraySize=tk.Entry(Array,textvariable=size)
ArraySize.grid(row=5,column=1)

SizeofArray=tk.Button(Array,text="Submit",command=Boxes)
SizeofArray.grid(row=5,column=2,sticky="w")



############################





root.mainloop()
