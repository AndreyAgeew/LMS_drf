from rest_framework.viewsets import ModelViewSet
from course.models import Course
from course.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.prefetch_related('lesson_set').all()
    serializer_class = CourseSerializer
