from django.db import models

# Commands to generate table
# python manage.py makemigrations books
# python manage.py sqlmigrate books 0001
# ython manage.py migrate



class Book(models.Model):

    def __str__(self):
        return self.name + ' by ' + self.author

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    type = models.CharField(max_length=100)