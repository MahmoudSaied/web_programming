from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    today = datetime.now()
    logic = today.month == 1 and today.day ==1
    return render(request, "new_year/home.html", {
        "new_year": logic
    })