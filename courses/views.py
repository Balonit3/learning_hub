from django.shortcuts import render,get_object_or_404
from .models import Course,Lesson

def course_detail(request,course_id):
    course = get_object_or_404(Course,pk=course_id)
    lessons = course.lessons.all()
    return render(request,'courses/course_detail.html',{'course':course,'lessons':lessons})

def course_list(request):
    courses = Course.objects.all()
    return render(request,'courses/course_list.html',{'course':courses})

