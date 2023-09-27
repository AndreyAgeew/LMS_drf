from rest_framework.generics import ListAPIView

from course.models import Lesson
from course.serializers.lesson import LessonSerializer


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
