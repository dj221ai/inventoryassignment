from django.db import models
from django.conf import settings


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

    @property
    def get_remaining(self):
        productquants = self.cartitem_set.all()
        remaining = sum([item.remaining_quantity_in_inventory for item in productquants])
        return remaining


class Cart(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.get_total for item in cartitems])
        return total

    @property
    def get_cart_items(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.quantity for item in cartitems])
        return total

    # @property
    # def get_remaining(self):
    #     product_quants = self.cartitem_set.all()
    #     remaining = sum([item.remaining_quantity_in_inventory for item in product_quants])
    #     return remaining


class CartItem(models.Model):
    product = models.ForeignKey(ProductInformation, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.product_name

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    @property
    def remaining_quantity_in_inventory(self):
        remaining_quantity = self.product.quantity - self.quantity
        # print('remaining_quantity', remaining_quantity)
        return remaining_quantity



