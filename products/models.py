from django.db import models

# Create your models here.
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(default='No summary available.')
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"id": self.id})
        # return f"/products/{self.id}"