from django import forms
from .models import Class, Subject
from django.db.models import Sum, Count
 

class SearchTeacher(forms.Form):
    """Form for searching teacher"""

    teacher = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Search Teacher Name:"})
        )

    def save(self, query):
        teacher = Class.objects.filter_teachers(query)
        return teacher


class SearchSubject(forms.Form):
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(),
        empty_label="Select a Subject"
        )

    def save(self, query):
        subject = Class.objects.filter_subject(query)
        teachers = subject.aggregate(Count("teacher", distinct=True))
        students = subject.aggregate(Count("students", distinct=True))
        total_hours = subject.aggregate(Sum("subject__total_duration"))
        return dict(teachers=teachers, students=students, total_hours=total_hours)
