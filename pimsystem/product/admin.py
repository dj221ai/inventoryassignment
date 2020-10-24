from django.contrib import admin
from .models import ProductInformation, Cart, CartItem

admin.site.register(ProductInformation)
admin.site.register(Cart)
admin.site.register(CartItem)
