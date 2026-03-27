from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)
def getWeather():
    city = textfield.get()
    try:
        geolocator = Nominatim(user_agent="myweatherapp123", timeout=10)
        location = geolocator.geocode(city)
        if location is None:
            messagebox.showerror("Error", "City not found!")
            return

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

      #weather
        lat = location.latitude
        lon = location.longitude
        api_key = "YOUR_API_KEY"
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
        json_data = requests.get(api).json()


        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=f"{temp}°")
        c.config(text=f"{condition} | FEELS LIKE {temp}°")
        w.config(text=f"💨 {wind} m/s")
        h.config(text=f"💧 {humidity} %")
        d.config(text=f"🌤 {description}")
        p.config(text=f"🔽 {pressure} hPa")

        except Exception as e:
        messagebox.showerror("Error", f"Could not retrieve data:\n{e}")

#search box

search_image = PhotoImage(file="C:\weather application in python\search.png")
myimage=Label(image=search_image)
myimage.place(x=20,y=20)
textfield=tk.Entry(root,justify="center",width=17,font=("poppin",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()
search_icon= PhotoImage(file="C:\weather application in python\search_icon.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)


#logo

logo_iage= PhotoImage(file="C:\weather application in python\logo_2-removebg-preview.png")
logo=Label(image=logo_iage)
logo.place(x=150,y=100)
# bottom box

Frame_image = PhotoImage(file=r"C:\weather application in python\bottom.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=10, side="bottom")

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)



#label

label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=100, y=355)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=227, y=355)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=355)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=355)

t= Label(font=("arial",70,'bold'), fg= "#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...", font=("arial", 20, 'bold'), bg="#1ab5ef")
w.place(x=30, y=430)

h=Label(text="...", font=("arial", 20, 'bold'), bg="#1ab5ef")
h.place(x=230, y=430)

d=Label(text="...", font=("arial", 20, 'bold'), bg="#1ab5ef")
d.place(x=420, y=430)

p=Label(text="...", font=("arial", 20, 'bold'), bg="#1ab5ef")
p.place(x=620, y=430)


root.mainloop()
