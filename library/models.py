# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Books(models.Model):
    book_id = models.CharField(max_length=10, primary_key=True)    
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author')
    isbn = models.IntegerField()
    publisher = models.ForeignKey('Publisher')

    def __str__(self):
        return self.book_id + " - " + self.title

    def __unicode__(self):
        return self.book_id + " - " + self.title

    class Meta:
        ordering = ['title']

class Author(models.Model):
    firstname = models.CharField(max_length=200)
    middlename = models.CharField(max_length=200, blank=True, null=True)
    lastname = models.CharField(max_length=200)
    dob = models.DateField()

    def __str__(self):
        return "Author " + self.firstname + " " + self.lastname

    def __unicode__(self):
        return "Author " + self.firstname + " " + self.lastname

    class Meta:
        ordering = ['lastname']

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " " + self.country

    def __unicode__(self):
        return self.name + " " + self.country

    class Meta:
        ordering = ['name']