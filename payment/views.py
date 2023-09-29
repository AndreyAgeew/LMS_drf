from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer
from .filters import PaymentFilter


class PaymentViewSet(viewsets.ModelViewSet):
    """
        ViewSet для взаимодействия с моделью платежа.

        Attributes:
            queryset (QuerySet): Набор объектов платежей.
            serializer_class (PaymentSerializer): Сериализатор, используемый для преобразования объектов платежей в JSON и наоборот.
            filter_backends (list): Список используемых бэкендов для фильтрации (используется только DjangoFilterBackend).
            filterset_class (PaymentFilter): Класс фильтра для применения фильтров к набору объектов платежей.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter
