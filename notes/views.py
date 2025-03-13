from django.shortcuts import render
from .models import Note

# Create your views here.
def index_view(request):
    name = "Nicola"
    # email = "gmail@nicola.id"
    notes = Note.objects.all()
    return render(request, "index.html", {"name": name, "notes": notes})
    # countries = ["Indonesia", "Malaysia", "Singapore", "Thailand", "Vietnam", "Philippines"]
    # return render(request, "index.html", {"name": name, "countries": countries, "email": email})
