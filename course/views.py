from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

import course
from course.models import Course

# Create your views here.

@login_required
def course_list(request, ):
    courses= Course.objects.all()

    if request.user.is_authenticated:
        for course in course:
            course.is_valid = request.user in course.subscribers.all()
    else:
        for course in course:
            course.is_valid = False

    context ={
        "courses": courses
    }
    return render (request, "course_list.html" , context)

@login_required
def course_detail(request, course_id ):
    course = get_object_or_404(Course, id =course_id)

    if request.user not in course.subscribers.all():
        return redirect("course_list")
    context={
        "course": course
    }
    return render (request, "course_detail.html" context)