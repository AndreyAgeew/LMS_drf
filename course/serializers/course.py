from rest_framework import serializers

from course.models import Course, Subscription
from course.serializers.lesson import LessonSerializer
from payment.services import get_payment_link


class CourseSerializer(serializers.ModelSerializer):
    """
        Сериализатор модели курса для использования в Django REST framework.

        Attributes:
            num_lessons (int): Количество уроков в курсе, вычисляется автоматически при сериализации.
            lessons (LessonSerializer): Сериализатор для связанных уроков, доступен только для чтения.
            is_subscribed (bool): Признак подписки на курс

        Meta:
            model (Course): Модель, которая используется для сериализации.
            fields (str): Поля, которые будут сериализованы (все поля).

        Methods:
            get_num_lessons(obj): Метод для вычисления количества уроков в курсе.
             get_is_subscribed(obj): Метод для проверки подписан ли пользователь на курс.
    """
    num_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')
    is_subscribed = serializers.SerializerMethodField()
    payment_url = serializers.SerializerMethodField()

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

    def get_is_subscribed(self, obj):
        """
            Возвращает информацию о том, подписан ли пользователь на обновления курса.

            Parameters:
                obj (Course): Экземпляр модели курса.

            Returns:
                bool: Признак подписки на курс.
        """
        user = self.context['request'].user

        return Subscription.objects.filter(user=user, course=obj).exists()

    def get_payment_url(self, instance):
        payment_data = get_payment_link(instance)
        return payment_data
