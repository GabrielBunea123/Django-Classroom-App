from django import forms
from django.forms import ModelForm
from .models import Room,Upload_Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Upload_Task
        fields = ('title','task')

from django import forms

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))