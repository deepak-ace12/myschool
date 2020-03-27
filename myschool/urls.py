from django.urls import path

from . import views

urlpatterns = [
    path("get_class_info", views.get_class_info, name="get_class_info"),
    path("search_teacher", views.SearchTeacherFormView.as_view(), name="search_teacher"),
    path("get_teachers_by_salaries", views.get_teachers_by_salaries, name="get_teachers_by_salaries"),
    path("search_subject", views.SearchSubjectFormView.as_view(), name="search_subject"),
]