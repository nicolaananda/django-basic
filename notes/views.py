from django.shortcuts import render
from .models import Note

# Create your views here.
def index_view(request):
    name = "Nicola"
    notes = Note.objects.all()
    return render(request, "index.html", {"name": name, "notes": notes})