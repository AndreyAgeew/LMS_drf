from rest_framework import serializers

from course.models import Course
from course.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    """
        Сериализатор модели курса для использования в Django REST framework.

        Attributes:
            num_lessons (int): Количество уроков в курсе, вычисляется автоматически при сериализации.
            lessons (LessonSerializer): Сериализатор для связанных уроков, доступен только для чтения.

        Meta:
            model (Course): Модель, которая используется для сериализации.
            fields (str): Поля, которые будут сериализованы (все поля).

        Methods:
            get_num_lessons(obj): Метод для вычисления количества уроков в курсе.
    """
    num_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')

    class Meta:
        model = Course
        fields = '__all__'

    def get_num_lessons(self, obj):
        """
            Возвращает количество уроков в курсе.

            Parameters:
                obj (Course): Экземпляр модели курса.

            Returns:
                int: Количество уроков в курсе.
        """
        return obj.lesson_set.count()
