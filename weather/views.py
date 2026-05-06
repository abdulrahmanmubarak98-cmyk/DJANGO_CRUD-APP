from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
from django.conf import settings
from weather.models import SearchHistory


@login_required
def weather_view(request):
    context = {}

    history = SearchHistory.objects.filter(user=request.user).order_by("-searched_at")

    context["history"] = history
    if request.method == "POST":
        city = request.POST.get("city")

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=1cff9cb3fd9166e2d44fd5b563ac8283"

        response = requests.get(url)
        data = response.json()

        if str(data.get("cod")) != "200":
            context["error"] = data.get("message", "City not found")
        else:

            temp = data["main"]["temp"] - 273.15
            description = data["weather"][0]["description"]
            humidity = data["weather"][0]["description"]

            SearchHistory.objects.create(user=request.user, city=city)

            context = {
                "city": city,
                "temperature": round(temp, 2),
                "description": description,
                "history": history,
            }

        return render(request, "weather/index.html", context)

    return render(request, "weather/index.html")
