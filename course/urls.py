from rest_framework import routers
from django.urls import path
from course.views.course import CourseViewSet
from course.views.lesson import LessonListAPIView

app_name = 'curse'

router = routers.SimpleRouter()
router.register('course', CourseViewSet)
urlpatterns = [
                  path('lesson/', LessonListAPIView.as_view(), name='lesson-list')
              ] + router.urls
