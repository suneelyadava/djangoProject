from django.shortcuts import render

from rest_framework import viewsets
from .models import Course
from .serelizer import CourseSerelizer


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerelizer
