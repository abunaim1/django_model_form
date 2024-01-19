from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name' : 'Student Name',
            'roll' : 'Student Roll'
        }
        widgets = {
            'name' : forms.TextInput()
        }
        help_texts = {
            'name' : 'Write with capital letter'
        }
        error_messege = {
            'name' : {'required' : 'Your name must'}
        }
