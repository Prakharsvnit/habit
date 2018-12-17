from django import forms
from .models import Habit

class habitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = '__all__'