from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.idpage, name = "idpage"),
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("gallery/", views.imagedisplay, name="gallery"),
]
