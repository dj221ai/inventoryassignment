from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import ProductInformation, CartItem, Cart
from .forms import ProductForm
import json


class ProductCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = 'product/product_create.html'
    success_url = '/product/productList/'

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class()


class ProductListView(LoginRequiredMixin, ListView):
    model = ProductInformation
    template_name = 'product/product_list.html'

    def get(self, request, *args, **kwargs):
        context = {}
        quantities = ProductInformation.objects.all()
        context['object_list'] = quantities
        customer = request.user
        cart, created = Cart.objects.get_or_create(customer=customer)
        cartItems = cart.get_cart_items
        context['cartItems'] = cartItems
        return render(request, self.template_name, context=context)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProductForm
    queryset = ProductInformation.objects.all()
    template_name = 'product/product_create.html'
    success_url = reverse_lazy('product:productList')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(ProductInformation, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductInformation
    success_url = reverse_lazy('product:productList')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(customer=customer)
        items = cart.cartitem_set.all()
        cartItems = cart.get_cart_items
    else:
        items = []
        cart = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = cart['get_cart_items']

    context = {'items': items, 'cart': cart, 'cartItems': cartItems}
    return render(request, 'product/cart.html', context)


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(productId, action)
    customer = request.user
    product = ProductInformation.objects.get(id=productId)
    cart, created = Cart.objects.get_or_create(customer=customer)

    cartItem, created = CartItem.objects.get_or_create(cart=cart, product=product)

    # remaining_items = CartItem.objects.all()
    # for r in remaining_items:
    #     print('r.quantity is', r.quantity, r.remaining_quantity_in_inventory)

    # for item in remaining_items:
    #     print('r.quantity is', item.remaining_quantity_in_inventory)

    if action == 'add':
        cartItem.quantity = (cartItem.quantity + 1)
    elif action == 'remove':
        cartItem.quantity = (cartItem.quantity - 1)
    elif action == 'delete':
        cartItem.quantity = 0
        cartItem.delete()

    cartItem.save()

    if cartItem.quantity <= 0:
        cartItem.delete()
    return JsonResponse("data has been updated!!", safe=False)





