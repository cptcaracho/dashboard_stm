from django.urls import path
from django.conf import settings
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.AppView.as_view(), name='app'),

]
