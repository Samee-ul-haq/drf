from django.urls import path
from .views import home
from .views import contact

urlpatterns = [
    path("", home, name="home"),
    path("contacts",contact,name="contacts")
]