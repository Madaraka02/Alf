from django import forms
from .models import *

from django import forms
from datetime import date


today = date.today()
class DatePickerInput(forms.DateInput):
    input_type = 'date'


class BookDestinationForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('user','park',)
        widgets = {
            'date' : DatePickerInput(attrs={'min': today}),
        }



class AttractionForm(forms.ModelForm):
    more_attraction_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
                    'class':'form-control',
                    'multiple':True
                    }))
    class Meta:
        model = Attraction
        # fields = '__all__'  
        exclude=('likes',)      

class ParkForm(forms.ModelForm):
    more_destination_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
                    'class':'form-control',
                    'multiple':True
                    }))
    class Meta:
        model = Park
        fields = '__all__'     

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'                   

class VisitAttractionForm(forms.ModelForm):
    class Meta:
        model=VisitAttraction
        exclude=('attraction','user')   
        widgets = {
            'date' : DatePickerInput(attrs={'min': today}),
        }     