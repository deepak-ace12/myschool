
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View
from django.db.models import Sum, Count

from .models import (
    Teacher,
    Student,
    ClassRoom,
    Subject,
    Relative,
    Class,
)
from myschool.forms import SearchTeacher, SearchSubject


def get_class_info(request):
    classes = Class.objects.all()
    context = {"classes": classes}
    return render(request, "myschool/classroom_details.html", context)


class SearchTeacherFormView(View):

    def get(self, request, *args, **kwargs):
        form = SearchTeacher()
        return render(request, 'myschool/search_teacher.html', {'form': form})

    def post(self, request, *args, **kwargs):
        context = {}
        form = SearchTeacher(request.POST)
        context.update({'form': form})
        if form.is_valid():
            query = form.cleaned_data.get("teacher")
            classes = form.save(query=query)
            context.update({"class": classes})
        return render(request, 'myschool/search_teacher.html', context)


def get_teachers_by_salaries(request):
   
    salary_lower_cap = 1200000
    teachers = Teacher.objects.filter(salary__gte=salary_lower_cap)
    total_salaries = teachers.aggregate(Sum("salary"))
    classes = Class.objects.filter(teacher__in=teachers)
    total_students = classes.aggregate(Count("students", distinct=True))
    total_salary_per_month = total_salaries.get('salary__sum')/12
    context = {
        "total_students": total_students,
        "total_salary_per_month": total_salary_per_month,
        "teachers": teachers,
    }
    return render(request, "myschool/teachers_salaries.html", context)


class SearchSubjectFormView(View):

    def get(self, request, *args, **kwargs):
        form = SearchSubject()
        return render(request, 'myschool/search_subject.html', {'form': form})

    def post(self, request, *args, **kwargs):
        context = {}
        form = SearchSubject(request.POST)
        context.update({'form': form})
        if form.is_valid():
            query = form.cleaned_data.get("subject")
            context.update(form.save(query=query))
        return render(request, 'myschool/search_subject.html', context)
