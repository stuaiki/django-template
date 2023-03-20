from .views import indexPageView
from django.urls import path

urlpatterns = [
    path('', indexPageView, name="index")
]
