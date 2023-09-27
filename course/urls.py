from rest_framework import routers
from django.urls import path
from course.views.course import CourseViewSet
from course.views.lesson import LessonListAPIView, LessonCreateAPIView, LessonDestroyAPIView

app_name = 'course'

router = routers.SimpleRouter()
router.register('course', CourseViewSet)
urlpatterns = [
                  path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lesson/create', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson-delete'),

              ] + router.urls
