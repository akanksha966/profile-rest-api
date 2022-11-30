
from django.urls import path

from profile_flipkart import views

urlpatterns = [

    path('hello-view/', views.HelloApiVIew.as_view()),

]
