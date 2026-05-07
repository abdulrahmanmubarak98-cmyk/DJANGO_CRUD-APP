from django.shortcuts import render
from .models import Note
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404


@login_required
def create_note(request):
    notes = Note.objects.filter(user=request.user).order_by("-id")

    if request.method == "POST":
        content = request.POST.get("content")

        if content:
            Note.objects.create(user=request.user, content=content)

            return redirect("/dashboard/")
    return render(request, "playground/hello.html", {"notes": notes})


@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    return redirect("/dashboard/")


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


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Account created successfully. you can now log in. "
            )

            return redirect("/dashboard/")
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
