from django.contrib import admin
from django.forms import ModelForm

from .models import Course, Lesson, Category
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('instructor','title','description','category','ctreated')
    list_display_links = ('title','description')
    search_fields = ('title','description')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title','description','order')
    list_display_links = ('title','description')
    search_fields = ('title','description')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    list_display_links = ('title','description')
    search_fields = ('title','description')

admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Category,CategoryAdmin)
