from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """
       Сериализатор модели платежа для использования в Django REST framework.

       Attributes:
           class Meta: Метаинформация о сериализаторе.
               model (Payment): Модель, которая используется для сериализации.
               fields (str): Поля, которые будут сериализованы (все поля).
    """

    class Meta:
        model = Payment
        fields = '__all__'
