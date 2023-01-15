from django.urls import path
from . import views

urlpatterns =[
    path('', views.homepage, name='homepage'),
    path('registered/', views.registered_patients, name='registered'),
]