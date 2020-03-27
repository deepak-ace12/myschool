from django.contrib import admin
from .models import (
    Teacher,
    Student,
    ClassRoom,
    Subject,
    Relative,
    Class,
)


admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(ClassRoom)
admin.site.register(Subject)
admin.site.register(Relative)
admin.site.register(Class)