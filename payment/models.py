from django.db import models
from users.models import User


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    date = models.DateField(verbose_name="дата оплаты")
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name="оплаченный курс")
    lesson = models.ForeignKey('course.Lesson', on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name="оплаченный урок")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="сумма оплаты")

    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет'),
    ]
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHOD_CHOICES,
        default='cash',
        verbose_name="способ оплаты"
    )

    def __str__(self):
        return f'{self.user.email} - {self.date} - {self.amount}'
