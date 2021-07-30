from django.db import models
import re
import bcrypt
from django.contrib import messages
import datetime
from datetime import datetime
from datetime import date


class UserManager(models.Manager):
    def registration_validation(self, postData):
        errors={}

        date=datetime.today()
        new_date=datetime(date.year, date.month, date.day)

        name_regex= re.compile(r'^[a-zA-Z]+$')
        email_regex= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['length_fn']="First name must be at least two characters."
        elif not name_regex.match(postData['first_name']):
            errors['regex_fn']="First name must only contain letters."
        if len(postData['last_name']) < 2:
            errors['length_ln']="Last name must be at least two characters."
        elif not name_regex.match(postData['last_name']):
            errors['regex_ln']="Last name must only contain letters."
        if not email_regex.match(postData['email']):
            errors['email']="Please enter a valid email."
        email_check= User.objects.filter(email=postData['email'])
        if len(email_check) > 0:
            errors['unique_email']="This email is already being used. Please enter a different email address."
        if len(postData['password']) < 8:
            errors['length_pwd']="Password must be at least 8 characters."
        elif postData['password'] != postData['password_conf']:
            errors['password']="Passwords must match."
        return errors

    def login_validation(self, postData):
        errors={}
        #Check if email is in database as registered user and return array of matches.
        login_user=User.objects.filter(email=postData['email'])
        email_regex= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        #If filtering results in a match 
        if len(postData['email']) == 0:
            errors['missing_email']="Please enter an email address."
        elif not email_regex.match(postData['email']):
            errors['email']="Please enter a valid email."
        elif len(login_user) == 0:
            errors['email']="There is no user with that email."
        if len(postData['password']) == 0:
            errors['missing_password']="Please enter a password."
        elif len(login_user) > 0:
            #Check to see if password entered matches password in database.
            if not bcrypt.checkpw(postData['password'].encode(), login_user[0].password.encode()):
                errors['password']="Password does not match."
        return errors

    def update_user(self, postData, user_email):
        errors= {}
        email_check= User.objects.filter(email=postData['email'])
        email_regex= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(postData['email']):
            errors['email']="Please enter a valid email."
        elif email_check[0].email != user_email:
            errors['email']="Email is already being used by another user."
        if len(postData['first_name']) < 2:
            errors['length_fn']="First name must be at least two characters."
        return errors


class User(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=80) #unique=True
    password=models.CharField(max_length=60)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

# Create your models here.
