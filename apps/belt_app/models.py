# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import bcrypt

class UserManager(models.Manager):

  def login(self, POST):
    errors = []
    if len(self.filter(email=POST['email'])) > 0:            
        user = self.filter(email=POST['email'])[0]
        if not bcrypt.checkpw(POST['password'].encode(), user.password.encode()):
            errors.append('email/password incorrect')
    else:
        errors.append('email/password incorrect')

    if len(errors)>0:
        return (False, errors)
    else:
        return (True, user)

  def validate(self, POST):
    errors = []
    if len(POST['name'])<2:
        errors.append('First name is required!')
    if len(POST['alias'])<2:
        errors.append('Alias is required!')
    if len(POST['email'])<2:
        errors.append('Email is required!') 
    elif not EMAIL_REGEX.match(POST['email']):
        errors.append('Email is not valid!')     
    elif len(User.objects.filter(email = POST['email']))>0:
        errors.append('Email already exists!')
    if len(POST['password'])<2:
        errors.append('Password is empty!') 
    elif POST['c_password'] != POST['password']:
        errors.append('Password does not match!')
    if len(errors)>0: 
      return (False, errors)
    else:
        new_user = User.objects.create(
            name = POST['name'],
            alias = POST['alias'],
            email = POST['email'],
            password = bcrypt.hashpw(POST['password'].encode(), bcrypt.gensalt())
        ) 
        print new_user
        return (True, new_user)
      # return the info so it can be obtained from here to views


class User(models.Model):
      name = models.CharField(max_length=255)
      alias = models.CharField(max_length=255)
      email = models.CharField(max_length=255)
      password = models.CharField(max_length=255)
      objects = UserManager()
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      def __repr__(self):
        return "<Blog object: {} {}>".format(self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    rating = models.IntegerField()
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Review(models.Model):
    review_title = models.CharField(max_length=255)
    review = models.TextField(default='null')
    book = models.ForeignKey(Book, related_name="reviews")
    user = models.ForeignKey(User, related_name="user_reviews")
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)