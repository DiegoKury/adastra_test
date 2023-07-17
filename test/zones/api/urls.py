from django.urls import path

from zones.api import views

urlpatterns = [
    path('api/put', views.edit), # New path added
]
