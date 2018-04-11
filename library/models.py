# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    book_id = models.CharField(max_length=10, blank=False, primary_key=True)    
    title = models.CharField(max_length=200, blank=False)
    author = models.ForeignKey('Author')
    isbn = models.BigIntegerField(blank=False)
    publisher = models.ForeignKey('Publisher')

    def __str__(self):
        return self.book_id + " - " + self.title

    def __unicode__(self):
        return self.book_id + " - " + self.title

    class Meta:
        ordering = ['title']

class Author(models.Model):
    firstname = models.CharField(max_length=200, blank=False)
    lastname = models.CharField(max_length=200, blank=False)
    dob = models.DateField(blank=False)

    def __str__(self):
        return self.firstname + " " + self.lastname

    def __unicode__(self):
        return self.firstname + " " + self.lastname

    class Meta:
        ordering = ['lastname']

class Publisher(models.Model):
    name = models.CharField(max_length=200, blank=False)
    country = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name + " " + self.country

    def __unicode__(self):
        return self.name + " " + self.country

    class Meta:
        ordering = ['name']

class Student(models.Model):
    male = 'Male'
    female = 'Female'
    it = 'IT'
    ece = 'ECE'

    GENDER_CHOICES = (
        (male, 'Male'),
        (female, 'Female'),
    )

    BRANCH_CHOICES = (
        (it, 'IT'),
        (ece, 'ECE'),
    )

    SEMESTER_CHOICES = (
        (1, '1st'),
        (2, '2nd'),
        (3, '3rd'),
        (4, '4th'),
        (5, '5th'),
        (6, '6th'),
        (7, '7th'),
        (8, '8th'),
        (9, '9th'),
        (10, '10th'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_no = models.CharField(max_length=10, blank=False)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    department = models.CharField(max_length=10, choices=BRANCH_CHOICES)
    semester = models.IntegerField(choices=SEMESTER_CHOICES)

    def __str__(self):
        return self.user.username + " " + self.enrollment_no

    def __unicode__(self):
        return self.user.username + " " + self.enrollment_no

    class Meta:
        ordering = ['semester']

class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    librarian_id = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.user.username + " " + self.librarian_id

    def __unicode__(self):
        return self.user.username + " " + self.librarian_id

    class Meta:
        ordering = ['first_name']
