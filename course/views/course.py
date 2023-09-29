from rest_framework.viewsets import ModelViewSet
from course.models import Course
from course.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    """
        ViewSet для взаимодействия с моделью курса.

        Attributes:
            queryset (QuerySet): Набор объектов курсов, включая предварительно загруженные связанные уроки.
            serializer_class (CourseSerializer): Сериализатор, используемый для преобразования объектов курса в JSON и наоборот.
    """
    queryset = Course.objects.prefetch_related('lesson_set').all()
    serializer_class = CourseSerializer
