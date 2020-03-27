from django.contrib import admin
from django.urls import path, include, re_path
from myschool import urls as school_urls
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="myschool/base.html"), name="home"),
    re_path(r"", include((school_urls, "myschool"), namespace="myschool")),
]
