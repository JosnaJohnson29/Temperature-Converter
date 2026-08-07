from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2dc84e4fb970658c88a4894bc8bcabdf").json()
    w_Label1.config(text=data['weather'][0]['main'])
    wb_Label1.config(text=data['weather'][0]['description'])
    temp_Label1.config(text=str(int(data['main']['temp']-273.15)))
    per_Label1.config(text=data['main']['pressure'])

win = Tk()
win . title("Wscube Tech")
win . config(bg = "blue")
win . geometry("500x570")

name_Label = Label(win,text="Wscube Weather App",font=("Time New Romen",30,"bold"))
name_Label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
List_name = [ "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", 
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", 
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", 
    "Uttar Pradesh", "Uttarakhand", "West Bengal"]
com =ttk.Combobox(win,text="Wscube Weather App", values=List_name,font=("Time New Romen",20,"bold"),textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

w_Label = Label(win,text="Weather Climate",font=("Time New Romen",20,))
w_Label.place(x=25, y=260, height=50, width=210)

w_Label1 = Label(win,text="",font=("Time New Romen",20,))
w_Label1.place(x=250, y=260, height=50, width=210)

wb_Label = Label(win,text="Weather Description",font=("Time New Romen",16))
wb_Label.place(x=25, y=330, height=50, width=210)

wb_Label1 = Label(win,text="",font=("Time New Romen",17))
wb_Label1.place(x=250, y=330, height=50, width=210)

tem_Label = Label(win,text="Temperature",font=("Time New Romen",20,))
tem_Label.place(x=25, y=400, height=50, width=210)

tem_Label1 = Label(win,text="",font=("Time New Romen",20,))
tem_Label1.place(x=250, y=400, height=50, width=210)

per_Label = Label(win,text="Pressure",font=("Time New Romen",20,))
per_Label.place(x=25, y=470, height=50, width=210)

per_Label1 = Label(win,text="",font=("Time New Romen",20,))
per_Label1.place(x=250, y=470, height=50, width=210)

done_button = Button(win,text="Done",font=("Time New Romen",20,"bold"),command=data_get)
done_button.place(x=200,y=190, height=50, width=100)

win.mainloop()
