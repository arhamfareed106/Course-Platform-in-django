from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),  # Root URL points to homepage
    path("courses/", views.course_list, name="course_list"),
    path("courses/<int:course_id>/", views.course_detail, name="course_detail"),
]
