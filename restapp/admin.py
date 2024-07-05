from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(BookModel)
admin.site.register(StudentModel)
admin.site.register(Taskmodel)