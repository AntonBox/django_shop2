from django.db import models
from root.base_models import TimedModel
from apps.catalog.models import Product
from django.contrib.auth.models import User


class CartItem(TimedModel):
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField()


class Cart(TimedModel):
    OPEN = 'open'
    CLOSED = 'closed'
    status_choice = ((OPEN, 'Open'), (CLOSED, 'Closed'))
    user = models.ForeignKey(User)
    status = models.CharField(max_length=6,
                              choices=status_choice, default=CLOSED)

    def __str__(self):
        return self.status