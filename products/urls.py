from django.urls import path

from products.views import (IndexView, ProductsListView, basket_add,
                            basket_remove)

app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('category/<int:category_id>', ProductsListView.as_view(), name='category'),
    path('page/<int:page>', ProductsListView.as_view(), name='paginator'),
    path('products/add/<int:product_id>/', basket_add, name='basket_add'),
    path('products/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
