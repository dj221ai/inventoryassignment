from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import ProductInformation
from .forms import ProductForm


class ProductCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = 'product/product_create.html'
    success_url = '/product/productList/'

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class()


class ProductListView(LoginRequiredMixin, ListView):
    model = ProductInformation
    template_name = 'product/product_list.html'

    # def get_queryset(self):
    #     return ProductInformation.objects.filter(user=self.request.user)


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

