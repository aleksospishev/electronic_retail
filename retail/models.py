from django.core.exceptions import ValidationError
from django.db import models


class ContactInfo(models.Model):
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.email}, {self.city}, {self.street} {self.house_number}"


class RetailNode(models.Model):
    LEVEL_CHOICES = (
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    )

    name = models.CharField(max_length=255)
    contacts = models.OneToOneField(
        ContactInfo, on_delete=models.CASCADE, related_name="retail_node"
    )
    supplier = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL, related_name="clients"
    )
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def level(self):
        if not self.supplier:
            return 0
        return self.supplier.level() + 1

    def clean(self):
        if self.supplier == self:
            raise ValidationError("Поставщик не может сам себе поставлять.")

        if self.supplier and self.supplier.level() >= self.level():
            raise ValidationError("Уровень поставщика должен быть выше поучателя.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} (level {self.level()})"


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=100)
    release_date = models.DateField()
    node = models.ForeignKey(
        RetailNode, on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return f"{self.name} {self.model}"
