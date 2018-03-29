# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        return HttpResponse("Hi")
    else:
        return redirect('accounts/login')