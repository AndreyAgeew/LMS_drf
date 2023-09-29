from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

from course.models import Lesson
from course.serializers.lesson import LessonSerializer


class LessonListAPIView(ListAPIView):
    """
        Представление для получения списка всех уроков.

        Attributes:
            serializer_class (LessonSerializer): Сериализатор, используемый для преобразования объектов уроков в JSON.
            queryset (QuerySet): Набор объектов уроков, используемых для построения списка.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateAPIView(CreateAPIView):
    """
        Представление для создания нового урока.

        Attributes:
            serializer_class (LessonSerializer): Сериализатор, используемый для преобразования JSON в объект урока.
    """
    serializer_class = LessonSerializer


class LessonDestroyAPIView(DestroyAPIView):
    """
        Представление для удаления урока.

        Attributes:
            queryset (QuerySet): Набор объектов уроков, используемых для поиска урока, который нужно удалить.
    """
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(UpdateAPIView):
    """
        Представление для обновления урока.

        Attributes:
            serializer_class (LessonSerializer): Сериализатор, используемый для преобразования JSON в объект урока.
            queryset (QuerySet): Набор объектов уроков, используемых для поиска урока, который нужно обновить.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(RetrieveAPIView):
    """
        Представление для получения деталей урока.

        Attributes:
            serializer_class (LessonSerializer): Сериализатор, используемый для преобразования объекта урока в JSON.
            queryset (QuerySet): Набор объектов уроков, используемых для поиска урока, детали которого нужно получить.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
