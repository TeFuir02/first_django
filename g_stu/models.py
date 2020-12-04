from django.db import models

# Create your models here.

class Grade(models.Model):
    g_name = models.CharField(max_length=200)


class Student(models.Model):
    s_name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    emali = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    g = models.ForeignKey(Grade, on_delete=models.CASCADE)