from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_flag_url, name="get_flag_url")

]