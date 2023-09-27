from rest_framework import routers
from django.urls import path
from course.views.course import CourseViewSet
from course.views.lesson import LessonListAPIView, LessonCreateAPIView

app_name = 'curse'

router = routers.SimpleRouter()
router.register('course', CourseViewSet)
urlpatterns = [
                  path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lesson/create', LessonCreateAPIView.as_view(), name='lesson-create'),
              ] + router.urls
