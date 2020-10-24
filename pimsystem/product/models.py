from django.db import models


class ProductInformation(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    product_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name

    @property
    def imageURL(self):
        try:
            url = self.product_image.url
        except:
            url = ''
        return url
