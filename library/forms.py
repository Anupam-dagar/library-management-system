from django import forms
from .models import Student, Issue, Books
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user']

class BookForm(forms.ModelForm):
    widgets = {
		'request_issue': forms.CheckboxInput(attrs={'onclick':'this.form.submit();'})
	}
    class Meta:
        model = Books
        fields = ('request_issue',)
    