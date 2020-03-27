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
    Chapter,
    Class,
    )
from .forms import SearchTeacher, SearchSubject

def get_class_info(request):
    classes = Class.objects.all()
    context = {"classes": classes}
    return render(request, "myschool/classroom_details.html", context)


class SearchTeacherFormView(View):
    form_class = SearchTeacher
    template_name = 'myschool/search_teacher.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        context = {}
        form = self.form_class(request.POST)
        context.update({'form': form})
        if form.is_valid():
            query = form.cleaned_data.get("teacher")
            classes = form.save(query=query)
            context.update({"class":classes})
        return render(request, self.template_name, context)


def get_teachers_by_salaries(request):
    # @TODO- Create a form to search teachers by salary caps.
    # For now writing a hardcoded 1 LPA

    context = {}
    salary_lower_cap = 100000
    classes =  Class.objects.filter(teacher__salary__gt=salary_lower_cap)
    total_salaries = classes.aggregate(Sum("teacher__salary"))
    total_students = classes.aggregate(Count("students", distinct=True))
    total_teachers = classes.aggregate(Count("teacher", distinct=True))
    context.update(
        {"total_students": total_students,
         "total_salaries":total_salaries,
         "teachers": total_teachers,
         })
    return render(request, "myschool/teachers_salaries.html", context)

class SearchSubjectFormView(View):
    form_class = SearchSubject
    template_name = 'myschool/search_subject.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        context = {}
        form = self.form_class(request.POST)
        context.update({'form': form})
        if form.is_valid():
            query = form.cleaned_data.get("subject")
            context.update(form.save(query=query))
        return render(request, self.template_name, context)
