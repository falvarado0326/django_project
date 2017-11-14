# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages

from django.shortcuts import render, HttpResponse, redirect
  
from .models import User, Book, Review
def index(request):
    return render(request, 'belt_app/index.html')

def books(request):
    user =  User.objects.login(request.POST)
    return render(request, 'belt_app/books.html', user)

def add_book(request):
    user =  User.objects.login(request.POST)
    return render(request, 'belt_app/add_book.html', user)

def reviews(request, id):
    user =  User.objects.login(request.POST)
    return render(request, 'belt_app/book_reviews.html', user)

def user(request, id):
    return render(request, 'belt_app/user.html')

def register(request):
    result = User.objects.validate(request.POST)
    if result[0]:
        return redirect('/')
    else:
        for error in result[1]:
            messages.add_message(request, messages.INFO, error)
        return redirect('/')
def login(request):
    result =  User.objects.login(request.POST)
    if result[0]:
        return redirect('/books')
    else:
        for error in result[1]:
            messages.add_message(request, messages.INFO, error)
        return redirect('/')
