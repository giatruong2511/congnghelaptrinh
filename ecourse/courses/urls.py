from django.db import router
from django.urls import path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('courses', views.CourseViewsets)

urlpatterns = [
    path('', include(routers.urls)),
]