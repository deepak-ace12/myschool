from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_joining = models.DateField()
    subjects = models.ManyToManyField("Subject")
    salary = models.FloatField(validators=[MinValueValidator(1.0)])
    web_lecture = models.BooleanField(default=False) 

    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_joining = models.DateField()
    standard = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    roll_no = models.PositiveIntegerField(unique=True)
    rank = models.PositiveIntegerField()
    point_of_contact = models.ManyToManyField("Relative")

    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name


class ClassRoom(models.Model):
    SHAPES = (
        ("OVAL", "Oval"), 
        ("RECTANGULAR", "Rectangular"),
        ("CANOPY", "Canopy"),
        ("ELEVATED", "Elevated"), 
    )

    seating_capacity = models.IntegerField(
        default=15, validators=[MinValueValidator(15)]
    )
    web_lecture_support = models.BooleanField(default=False)
    shape = models.CharField(max_length=20, choices=SHAPES)

    def __str__(self):
        return self.shape


class Subject(models.Model):
    name = models.CharField(max_length=40)
    chapters = models.ManyToManyField("Chapter")
    duration = models.IntegerField(
        default=30,
        validators=[MinValueValidator(10), MaxValueValidator(120)]
    )
    total_duration = models.IntegerField()

    def __str__(self):
        return self.name


class Relative(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=12)
    relation = models.CharField(max_length=20)
    
    
    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name


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

