from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def course_list(request, ):
    return render (request, "base.html")

@login_required
def course_detail(request, ):
    return render (request, "base.html")