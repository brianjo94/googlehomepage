from django.shortcuts import render, redirect
from django.urls import reverse
from .models import PatientName
from .forms import PatientInfoForm

# Create your views here.


def homepage(request):
    #If post request -> Check form contents -> Send to registered.html
    if request.method == 'POST':
        form = PatientInfoForm(request.POST)   #passing information written into the form
        if form.is_valid():
            print(form.cleaned_data)    # {'first_name' : 'brian",..} this can be something else, for this case we're using this. But we could link this to model/database and save
            return redirect(reverse('patients:registered'))

    #else then render forms
    else:
        form = PatientInfoForm()
    return render(request, 'patients/homepage.html', context = {'form':form})

def registered_patients(request):
    """show all registered patients"""
    name = PatientName.objects.all()
    context = {'name' : name}
    return render(request, 'patients/registered.html', context)