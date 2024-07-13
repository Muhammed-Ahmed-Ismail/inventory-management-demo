from django.core.validators import MinValueValidator
from django.db import models, transaction

from core.models import BaseModel
from products.models import Product
from warehouses.exceptions.not_sufficient_quantity_exception import NotSufficientQuantityException
from warehouses.models import Warehouse


class InventoryEntry(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'warehouse')

    def __str__(self):
        return f'{self.product} - {self.quantity}'

    @classmethod
    @transaction.atomic
    def add_product_to_warehouse(cls, product: "Product", quantity: int, warehouse: "Warehouse"):
        create_defaults = {'quantity': 0}
        inventory_entry, created = cls.objects.update_or_create(product=product, warehouse=warehouse, create_defaults=create_defaults)
        inventory_entry.quantity += quantity
        inventory_entry.save()
        return inventory_entry

    @classmethod
    @transaction.atomic
    def draw_product_from_warehouse(cls, product: "Product", quantity: int, warehouse: "Warehouse"):
        try:
            inventory_entry = cls.objects.get(product=product, warehouse=warehouse)
        except cls.DoesNotExist:
            raise cls.DoesNotExist()

        if inventory_entry.quantity < quantity:
            raise NotSufficientQuantityException(f'Not sufficient quantity of {product} in warehouse {warehouse}')
        inventory_entry.quantity -= quantity
        inventory_entry.save()
        return inventory_entry