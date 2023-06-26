from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task
from django import forms


class UserUpdatedForm(UserCreationForm):
    class Meta :
        model = User
        fields = ['username', 'password1','password2', 'email']
        labels = {'username':'Name' }

    def __init__(self, *args, **kwargs):
        super(UserUpdatedForm, self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control bg-light border border-danger'}) 

class Taskform(ModelForm):
    class Meta:
        model = Task
        fields = ['name','description','complete']
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control bg-light border border-danger'}),
                'description': forms.TextInput(attrs={'class': 'form-control bg-light border border-danger'}),
        }

 