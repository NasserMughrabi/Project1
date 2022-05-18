from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django import forms
from requests import request
from . import util

class newform(forms.Form):
    entry_title = forms.CharField(label="New Task")


def new(request):
    return render(request, "encyclopedia/new.html", {
        "form": newform()
    })

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new(request):
    return render(request, "encyclopedia/new.html", {
        "entries": util.list_entries()
    })

def random(request):
    return render(request, "encyclopedia/random.html", {
        "entries": util.list_entries()
    })

def search(request):
    if request.GET.get('q', '') in util.list_entries():
        return render(request, "encyclopedia/entry.html", {
        "entry":  util.get_entry(request.GET.get('q', '')),
        "entry_title": [request.GET.get('q', '')]
    })

    return render(request, "encyclopedia/search.html", {
        "query_entry": request.GET.get('q', ''),
        "entries": util.list_entries()
    })

def save_new(request):
    entry_title = request.GET.get('entryTitle', '')
    entry_content = request.GET.get('entryContent', '')
    if entry_title in util.list_entries():
        return HttpResponseBadRequest("ERROR: Entry already exists!")
    else:
        util.save_entry(entry_title, entry_content)
        return render(request, "encyclopedia/entry.html", {
            "title": entry_title,
            "entry": entry_content
        })

def edit(request, title):
    entry = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "entry": entry
    })

def save_edited(request):
    entry_title = request.GET.get('entryTitle', '')
    entry_content = request.GET.get('entryContent', '')
    util.save_entry(entry_title, entry_content)
    return render(request, "encyclopedia/entry.html", {
        "title": entry_title,
        "entry": entry_content
    })

def entry(request, entry):
    if not entry.isupper():
        entry = entry.capitalize()

    if util.get_entry(entry) is None:
        entry_result = "404 PAGE NOT FOUND"
    else:
        entry_result = util.get_entry(entry)

    return render(request, "encyclopedia/entry.html", {
        "entry": entry_result,
        "title": entry
    })

