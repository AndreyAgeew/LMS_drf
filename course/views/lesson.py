from rest_framework.generics import ListAPIView, CreateAPIView

from course.models import Lesson
from course.serializers.lesson import LessonSerializer


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer


class LessonDestroyAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
