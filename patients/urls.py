from django.urls import path
from . import views

app_name = 'patients'
urlpatterns =[
    path('', views.homepage, name='homepage'),
    path('registered/', views.registered_patients, name='registered'),
]