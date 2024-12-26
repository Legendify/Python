import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "YOUR_API_KEY"  # جایگزین با کلید API خود
    url = f'http://api.weatherapi.com/v1/current.json?key={WEATHER_KEY}&q={weather}&aqi=no'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        weather = f"City: {data['name']}\nTemperature: {data['main']['temp']}°C\nWeather: {data['weather'][0]['description']}"
        result_label.config(text=weather)
    else:
        result_label.config(text="City not found!")

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("Weather App")

# ورودی شهر
city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=5)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

# دکمه برای دریافت آب و هوا
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

# نمایش نتیجه
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# اجرای حلقه اصلی
root.mainloop()
