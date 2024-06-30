from .models import CodeDropDB
from django.forms import ModelForm, Textarea, TextInput, Select, DateInput, ChoiceField


class CodeDropForm(ModelForm):
    class Meta:
        model = CodeDropDB
        fields = ['name', 'prog_lang', 'date_removal', 'text']
        # fields = ['name', 'text']

        choices = [
            ('python', 'Python'),
            ('java', 'Java'),
            ('javascript', 'Javascript'),
            ('csharp', 'C#'),
            ('cpp', 'C++')
        ]

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control title-input',
                'placeholder': 'Name',
            }),
            'prog_lang': ChoiceField(choices=choices, attrs={
                'class': 'form-control',
                'placeholder': 'Programming Language (Optional)',
            }),
            'date_removal': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of deletion (Optional)',
            }),
            'text': Textarea(attrs={
                'class': 'form-control content-input',
                'placeholder': 'Code',
            })
        }
