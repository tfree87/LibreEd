from django.db import models


class Student(models.Model):
    """Represents data for a single student"""

    id_num = models.PositiveIntegerField("Student ID Number", primary_key=True)
    first_name = models.CharField("Student's First Name")
    last_name = models.CharField("Student's Last Name")
    age = models.PositiveIntegerField("Student's Age")
    student_email = models.EmailField("Student Email Address")

    def __str__(self):
        return self.last_name + ", " + self.first_name


class Course(models.Model):
    uuid4 = models.UUIDField()
    name = models.CharField()
    teacher = models.CharField()
    students_in_class = models.ManyToManyField(Student, through="Enrolled")

    def __str__(self):
        return self.name


class Enrolled(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()

    def __str__(self):
        return str(date_enrolled)
