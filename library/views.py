# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Books, Student, Librarian
from .forms import UserForm, StudentForm, BookForm
from django.contrib.auth.models import User
from django.http import JsonResponse
# Create your views here.
def home(request):
    if request.user.is_authenticated():
        try:
            query = request.GET.get('q')
        except ValueError:
            query = None
        if query:
            q_type = request.GET.get('type')
            if q_type == 'author':
                detail = Books.objects.filter(author__fullname__icontains=query)
            if q_type == 'title':
                detail = Books.objects.filter(title__icontains=query)
            if q_type == 'isbn':
                detail = Books.objects.filter(isbn=query)
            if q_type == 'users':
                detail = Student.objects.filter(fullname__icontains=query) or Librarian.objects.filter(fullname__icontains=query)
            # if detail:
            #     if request.method == "POST":
            #         form = IssueForm(request.POST)
            #         if form.is_valid():
            #             detail1 = form.save(commit=False)
            #             detail1.user = request.user
            #             detail1.user = 
            #             detail1.save()
            #             return HttpResponse("done")
            #         else:
            #         form = IssueForm
            if not detail:
                detail = ['No results found!']
            return render(request, 'library/index.html', {'detail': detail})            
        return render(request, 'library/index.html', {})
    else:
        return redirect('accounts/login')

def student_dashboard(request):
    detail = Books.objects.filter(request_issue=True)
    return render(request, 'library/student_dashboard.html', {'detail': detail})

def change_request_issue(request):
    request_issue = request.GET.get('request_val')
    bookid = request.GET.get('bookid')
    myobject = Books.objects.filter(book_id=bookid).exists()
    if myobject:
        Books.objects.filter(book_id=bookid).update(request_issue=request_issue)
        boolval = 'True'
    else:
        boolval = 'False'
    data = {
        'valdb': boolval
    }
    return JsonResponse(data)

def create_user(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                detail = form.save(commit=False)
                detail.save()
                return redirect('create_student', username=detail.username, staff=request.user.username)
        else:	
            form = UserForm
        return render(request, 'library/adminpage.html', {'form':form})
    else:
        return render(request,'library/index.html',{})

def create_student(request, username, staff):
    if request.user.username == staff:
        user_instance = get_object_or_404(User, username=username)
        if request.method == "POST":
            form = StudentForm(request.POST)
            if form.is_valid():
                detail = form.save(commit=False)
                detail.user = user_instance
                detail.save()
                return HttpResponse("done")
        else:
            form = StudentForm
        return render(request, 'library/adminpage.html', {'form':form})
    else:
        return render(request,'library/index.html',{})
