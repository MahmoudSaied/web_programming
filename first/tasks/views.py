from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
                  "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        submission = NewTaskForm(request.POST)
        if submission.is_valid():
            task = submission.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect("/tasks")
        else:
            return render(request, "tasks/add.html")

    return render(request, "tasks/add.html",{
        "form": NewTaskForm()
    })