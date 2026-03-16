from django.shortcuts import render
from .models import Note


def hello(request):

    if request.method == "POST":

        if "title" in request.POST:

            title = request.POST.get("title")
            Note.objects.create(title=title)

        if "delete_note" in request.POST:
            note_id = request.POST.get("delete_note")

            Note.objects.get(id=note_id).delete()

    notes = Note.objects.all()
    return render(request, "playground/hello.html", {"notes": notes})


def edit_note(request, id):
    note = Note.objects.get(id=id)

    if request.method == "POST":
        new_title = request.POST.get("title")
        note.title = new_title
        note.save()

    return render(request, "playground/edit.html", {"note": note})
