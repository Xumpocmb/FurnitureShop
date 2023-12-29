from django.db import models


class CartQueryset(models.QuerySet):
    # сколько всего стоит в корзине
    def total_price(self):
        return sum(cart.cart_cost() for cart in self)

    # сколько заказал пользователей
    def total_quantity(self):
        if self:
            return self.aggregate(models.Sum('quantity'))['quantity__sum']
        return 0


class Cart(models.Model):
    user = models.ForeignKey('users_app.User', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    session = models.CharField(max_length=128, blank=True, null=True, verbose_name='Сессия')
    product = models.ForeignKey('catalog_app.Product', on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ['id']

    objects = CartQueryset.as_manager()

    def cart_cost(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f'Корзина: {self.user.username} | Товар: {self.product.name}'
