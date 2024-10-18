from django.contrib import admin
from .models import User

class students(admin.ModelAdmin):
    list_of_student = ['user_id']

# Register your models here.
admin.site.register(User, students)
