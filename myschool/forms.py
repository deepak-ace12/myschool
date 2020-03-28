from django import forms
from .models import Class, Subject
from django.db.models import Sum, Count
 

class SearchTeacher(forms.Form):

    teacher = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Teacher's Name:"})
    )

    def save(self, query):
        teacher = Class.objects.filter_teachers(query)
        return teacher


class SearchSubject(forms.Form):
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.annotate(
            teacher_count=Count('teacher')
        ).filter(teacher_count__gt=1),
        empty_label="Select a Subject"
    )

    def save(self, query):
        subject = Class.objects.filter_subject(query)
        teachers = subject.aggregate(Count("teacher", distinct=True))
        students = subject.aggregate(Count("students", distinct=True))
        total_hours = subject.aggregate(
            Sum("subject__total_duration_in_hours")
        )
        return dict(
            teachers=teachers, students=students, total_hours=total_hours
        )
