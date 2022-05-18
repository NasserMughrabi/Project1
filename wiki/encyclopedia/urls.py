from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("save_new", views.save_new, name="save_new"),
    path("random", views.random, name="random"),
    path("<str:entry>", views.entry, name="entry")
]
