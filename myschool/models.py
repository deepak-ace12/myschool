from django.db import models
from .constants import Shape
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Teacher(models.Model):
    full_name = models.CharField(max_length=40)
    date_of_joining = models.DateField()
    subject = models.ManyToManyField("Subject")
    salary = models.FloatField(validators=[MinValueValidator(1.0)])
    web_lecture = models.BooleanField(default=False) 

    def __str__(self):
        return f"Teacher: {self.full_name}"


class Student(models.Model):
    full_name = models.CharField(max_length=40)
    date_of_joining = models.DateField()
    standard = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    roll_no = models.PositiveIntegerField(unique=True)
    rank = models.PositiveIntegerField()
    point_of_contact = models.ManyToManyField("Relative")

    def __str__(self):
        return f"Student: {self.full_name}"



class ClassRoom(models.Model):
    seating_capacity = models.IntegerField(default=15, validators=[MinValueValidator(15)])
    web_lecture_support = models.BooleanField(default=False)
    shape = models.CharField(max_length=20, choices=[(shape.name, shape.name) for shape in Shape])

    def __str__(self):
        return f"Classroom: {self.shape}"


class Subject(models.Model):
    name = models.CharField(max_length=40)
    chapters = models.ManyToManyField("Chapter")
    duration = models.IntegerField(default=30,validators=[MinValueValidator(30), MaxValueValidator(120)])
    total_duration = models.IntegerField()

    def __str__(self):
        return f"Subject: {self.name}"



class Relative(models.Model):
    full_name = models.CharField(max_length=40)
    contact_number = models.CharField(max_length=10)
    relation = models.CharField(max_length=40)

    def __str__(self):
        return f"Relative: {self.full_name}"


class Chapter(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"Chapter: {self.name}"

class ClassManager(models.Manager):

    def filter_teachers(self, teacher_name):
        return Class.objects.filter(teacher__full_name__icontains=teacher_name)

    def filter_subject(self, subject):
        return Class.objects.filter(subject=subject)


class Class(models.Model):
    room = models.ForeignKey("ClassRoom", on_delete=models.CASCADE)
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE)
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)
    students = models.ManyToManyField("Student")
    objects = ClassManager()

    def __str__(self):
        return f"Class: {self.subject.name} is taken by {self.teacher.full_name} in room {self.room.shape}" 


@receiver(m2m_changed, sender=Class.students.through)
def limit_minimum_students(sender, instance, **kwargs):
    if 0 < instance.students.count() < 15:
        raise ValidationError("You can't have less than 15 students in a class.")
    elif instance.students.count() > instance.room.seating_capacity:
        raise ValidationError("The class is overcrowded. No seating left. Please kick off some students.")