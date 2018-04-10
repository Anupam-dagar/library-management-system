# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Books

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        try:
            query = request.GET.get('q')
        except ValueError:
            query = None
        if query:
            detail = Books.objects.filter(author__firstname=query)
            if not detail.exists():
                detail = ['No results found!']
            return render(request, 'library/index.html', {'detail': detail})
        return render(request, 'library/index.html', {})
    else:
        return redirect('accounts/login')