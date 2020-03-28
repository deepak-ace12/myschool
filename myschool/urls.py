from django.urls import path

from . import views

urlpatterns = [
    path("class-info", views.get_class_info, name="class_info"),
    path(
        "search-teacher", 
        views.SearchTeacherFormView.as_view(), 
        name="search_teacher"
    ),
    path(
        "teachers-by-salaries", 
        views.get_teachers_by_salaries, 
        name="get_teachers_by_salaries"
    ),
    path(
        "search-subject", 
        views.SearchSubjectFormView.as_view(), 
        name="search_subject"
    ),
]