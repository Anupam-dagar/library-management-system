# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Books, Author, Publisher, Student, Librarian
# Register your models here.
admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Student)
admin.site.register(Librarian)