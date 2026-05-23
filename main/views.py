from django.shortcuts import render, redirect
from .models import Search
import requests

API_KEY = "488c8f6fc2602aaafb85080e9d7cd8eb"  # replace with your key

def home(request):
    weather = None
    forecast = []

    # Handle delete request
    if request.method == "POST" and 'delete_id' in request.POST:
        delete_id = request.POST.get('delete_id')
        Search.objects.filter(id=delete_id).delete()
        return redirect('home')

    # Handle new search
    if request.method == "POST" and 'city' in request.POST:
        city = request.POST.get("city")
        Search.objects.create(city=city)

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        data = requests.get(url).json()

        if data.get("cod") == 200:
            weather = {
                "city": city,
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"].title(),
                "icon": data["weather"][0]["icon"]
            }

            # 5-day forecast
            url2 = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
            forecast_data = requests.get(url2).json()
            forecast = []

            for i in range(0, 40, 8):  # every 24h
                day = forecast_data["list"][i]
                forecast.append({
                    "date": day["dt_txt"].split(" ")[0],
                    "temp": day["main"]["temp"],
                    "desc": day["weather"][0]["description"].title(),
                    "icon": day["weather"][0]["icon"]
                })
        else:
            weather = {"error": "City not found!"}

    searches = Search.objects.all().order_by('-searched_at')  # latest first
    return render(request, "home.html", {"weather": weather, "forecast": forecast, "searches": searches})
