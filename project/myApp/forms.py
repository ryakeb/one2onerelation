from django import forms
from myApp.models import Country, President, User, Project, Task, Question, Answer

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

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'mail': forms.EmailInput(attrs={'class':'form-control'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'user': forms.Select(attrs={'class':'form-control'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'project': forms.Select(attrs={'class':'form-control'}),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'question_text': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
        widgets = {
            'answer_text': forms.TextInput(attrs={'class':'form-control'}),
            'question': forms.Select(attrs={'class':'form-control'}),
            'is_correct': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }



