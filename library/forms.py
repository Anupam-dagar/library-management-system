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
    class Meta:
        model = Books
        fields = ('book_id', 'title', 'author', 'isbn', 'publisher')    