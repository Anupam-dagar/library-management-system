# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Books, Student, Librarian

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        try:
            print(request.GET)
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
            # if q_type == 'users':
            #     query = query.split()
            #     detail = User.objects.filter(first_name__icontains=query)
            if not detail:
                detail = ['No results found!']
            return render(request, 'library/index.html', {'detail': detail})            
        return render(request, 'library/index.html', {})
    else:
        return redirect('accounts/login')