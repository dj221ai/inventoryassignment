from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('create/', views.ProductCreateView.as_view(), name="create"),
    path('productList/', views.ProductListView.as_view(), name="productList"),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete'),
    path('cart/', views.cart, name='cart'),
    path('update_item/', views.update_item, name="update_item"),
]
