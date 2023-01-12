from django import forms

class PatientInfoForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100) #creates html label called first name
    last_name = forms.CharField(label='Last Name', max_length=100)
    ohip_number = forms.CharField(label='OHIP Number', max_length=100)
    reason_for_visit = forms.CharField(widget=forms.Textarea, label='Reason For Visit')
    email = forms.EmailField(label='Email')
