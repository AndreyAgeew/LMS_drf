from rest_framework import serializers
from course.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    """
       Сериализатор для модели подписки на курс.

       Attributes:
           model (Subscription): Модель, которая используется для сериализации.
           fields : Поля, которые будут сериализованы (все поля).
    """

    class Meta:
        model = Subscription
        fields = '__all__'
