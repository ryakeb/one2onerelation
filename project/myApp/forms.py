from django import forms
from myApp.models import Country, President

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
        
class PresidentForm(forms.ModelForm):
    class Meta:
        model = President
        fields = '__all__'
        widgets = {
            'img' : forms.FileInput(attrs={'class':'form-control'}),
            'url_img': forms.URLInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'sex': forms.Select(attrs={'class':'form-control'}),
        }