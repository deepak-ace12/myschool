from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    subjects = models.ManyToManyField("Subject")
    salary = models.FloatField(validators=[MinValueValidator(1.0)])
    takes_web_lecture = models.BooleanField(default=False) 

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=40)
    date_of_joining = models.DateField()
    standard = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    roll_no = models.PositiveIntegerField(unique=True)
    rank = models.PositiveIntegerField()
    point_of_contact = models.ManyToManyField("Relative")
    
    class Meta:
        unique_together = ("name", "roll_no")

    def __str__(self):
        return self.name


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
    has_web_lecture_support = models.BooleanField(default=False)
    shape = models.CharField(max_length=20, choices=SHAPES)

    def __str__(self):
        return self.shape


class Subject(models.Model):
    name = models.CharField(max_length=40, unique=True)
    chapters = models.PositiveIntegerField()
    per_class_duration = models.IntegerField(
        default=30,
        validators=[MinValueValidator(10), MaxValueValidator(120)]
    )
    total_duration_in_hours = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Relative(models.Model):
    name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=12)
    relation = models.CharField(max_length=20)
    
    class Meta:
        unique_together = ("name", "contact_number")
    
    def __str__(self):
        return self.name


class ClassManager(models.Manager):

    def filter_teachers(self, teacher_name):
        return Class.objects.filter(teacher__name__icontains=teacher_name)

    def filter_subject(self, subject):
        return Class.objects.filter(subject=subject)


class Class(models.Model):
    class_room = models.ForeignKey("ClassRoom", on_delete=models.CASCADE)
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE)
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)
    students = models.ManyToManyField("Student")
    objects = ClassManager()
    
    def __str__(self):
        return "{0} being taken in {1} class by {2}".format(
            self.subject, self.room, self.teacher
        )


@receiver(m2m_changed, sender=Class.students.through)
def limit_minimum_students(sender, instance, **kwargs):
    if 0 < instance.students.count() < 15:
        raise ValidationError("A class must have at least 15 students")
    elif instance.students.count() > instance.class_room.seating_capacity:
        raise ValidationError("The class is full.")


