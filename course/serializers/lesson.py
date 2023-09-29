from rest_framework import serializers

from course.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """
        Сериализатор модели урока для использования в Django REST framework.

        Attributes:
            class Meta: Метаинформация о сериализаторе.
                model (Lesson): Модель, которая используется для сериализации.
                fields (str): Поля, которые будут сериализованы (все поля).

    """

    class Meta:
        model = Lesson
        fields = '__all__'
