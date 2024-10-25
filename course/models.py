from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)
    instructor= models.ForeignKey(User, on_delete=models.CASCADE, related_name="course_taught")
    subscribers= models.ManyToManyField(User, related_name="course_subscribed", blank=True)
    price= models.DecimalField(max_digits=6, decimal_places=2, default=1.99) # type: ignore

    def __str__(self):
        return self.title