from django import forms
from .models import Task


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ["user"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "complete": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "importance": forms.Select(attrs={"class": "form-control"}),
        }


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["description", "importance"]

        widgets = {
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "importance": forms.Select(attrs={"class": "form-control"}),
        }
