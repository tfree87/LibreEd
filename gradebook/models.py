from django.db import models


class Gradebook(models.Model):
    course = models.ForeignKey("sis.Course")
    grades = models.ManyToManyField(Grade)


class Grade(models.Model):
    asessement = models.ForeignKey("assessment_creator.Assessment")
    student = models.ForeignKey("sis.Student")
    earned_points = models.PositiveIntegerField()
    max_points = models.PositiveIntegerField()
    excused = models.BooleanField()
    missing = models.BooleanField()
    incomplete = models.BooleanField()
    date_completed = models.DateTimeField()

    def __str__(self):
        return earned_points + "/" + max_points
