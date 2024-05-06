from django import forms
from django.core.exceptions import ValidationError
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic'] 
        widgets = { 
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_name(self):
        data = self.cleaned_data["name"]
        if len(data) < 1:
            raise ValidationError("Ім'я повинно містити хоча б одну літеру")
        return data
    def clean_surname(self):
        data = self.cleaned_data["surname"]
        if len(data) < 1:
            raise ValidationError("Прізвище повинно містити хоча б одну літеру")
        return data
    def clean_patronymic(self):
        data = self.cleaned_data["patronymic"]
        if len(data) < 1:
            raise ValidationError("Ім'я по батькові повинно містити хоча б одну літеру")
        return data
