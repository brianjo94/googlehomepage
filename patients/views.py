from django.shortcuts import render
from .models import PatientName

# Create your views here.


def homepage(request):
    return render(request, 'patients/homepage.html')

def registered_patients(request):
    """show all registered patients"""
    name = PatientName.objects.all()
    context = {'name' : name}
    return render(request, 'patients/registered.html', context)