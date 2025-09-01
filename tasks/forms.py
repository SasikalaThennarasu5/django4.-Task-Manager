from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "is_completed"]

# Manual form for filtering by date
class TaskFilterForm(forms.Form):
    due_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date"}))
