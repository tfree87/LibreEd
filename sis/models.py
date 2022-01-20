from django.db import models


class Student(models.Model):
    student_id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    student_email = models.EmailField()


class Class(models.Model):
    class_uuid4 = models.UUIDField()
    class_name = models.CharField(max_length=25)
