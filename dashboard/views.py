from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
from django.conf import settings
from weather.models import SearchHistory
from django.utils import timezone
from playground.models import Note
from django.shortcuts import redirect


@login_required
def dashboard_view(request):
    context = {}

    # ✅ LOAD DATA
    notes = Note.objects.filter(user=request.user).order_by("-id")
    history = SearchHistory.objects.filter(user=request.user).order_by("-searched_at")

    context["notes"] = notes
    context["history"] = history

    # ✅ HANDLE POST FIRST
    if request.method == "POST":

        # ➤ ADD NOTE
        if "add_note" in request.POST:
            content = request.POST.get("content")
            if content:
                Note.objects.create(user=request.user, content=content)
            return redirect("/dashboard/")

        # ➤ SEARCH WEATHER
        elif "search_weather" in request.POST:
            city = request.POST.get("city")
            if city:
                return redirect(f"/dashboard/?city={city}")

    # ✅ HANDLE WEATHER (GET)
    city = request.GET.get("city")

    if city:
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.WEATHER_API_KEY}"
            response = requests.get(url)
            data = response.json()

            if data.get("cod") != 200:
                context["error"] = data.get("message", "City not found")
            else:
                temp = data["main"]["temp"] - 273.15
                description = data["weather"][0]["description"]

                # ✅ ALWAYS SHOW WEATHER (FIXED)
                context.update(
                    {
                        "city": city,
                        "temperature": round(temp, 2),
                        "description": description,
                    }
                )

                # ✅ HANDLE HISTORY SEPARATELY
                history_item = SearchHistory.objects.filter(
                    user=request.user, city=city
                ).first()

                if history_item:
                    history_item.searched_at = timezone.now()
                    history_item.save()
                else:
                    SearchHistory.objects.create(user=request.user, city=city)

        except Exception:
            context["error"] = "Something went wrong"

    return render(request, "dashboard.html", context)


@login_required
def weather_view(request):
    context = {}

    history = SearchHistory.objects.filter(user=request.user).order_by("-searched_at")

    context["history"] = history

    if request.method == "POST":
        city = request.POST.get("city")

        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.WEATHER_API_KEY}"
            response = requests.get(url)
            data = response.json()

            if data.get("cod") != 200:
                context["error"] = data.get(
                    "message", "Please enter a valid city (e.g Lagos, Kano)"
                )
            else:
                temp = data["main"]["temp"] - 273.15
                description = data["weather"][0]["description"]

                # ✅ SAME DUPLICATE CONTROL
                history_item = SearchHistory.objects.filter(
                    user=request.user, city=city
                ).first()

                if history_item:
                    history_item.searched_at = timezone.now()
                    history_item.save()
                else:
                    SearchHistory.objects.create(user=request.user, city=city)

                context.update(
                    {
                        "city": city,
                        "temperature": round(temp, 2),
                        "description": description,
                    }
                )

    return render(request, "weather/index.html", context)


@login_required
def edit_note(request, note_id):
    note = Note.objects.get(id=note_id, user=request.user)

    if request.method == "POST":
        new_content = request.POST.get("content")

        if new_content:
            note.content = new_content
            note.save()
        return redirect("/dashboard/")
    return render(request, "playground/edit.html", {"note": note})


@login_required
def delete_note(request, note_id):
    note = Note.objects.get(id=note_id, user=request.user)
    note.delete()
    return redirect("/dashboard/")
