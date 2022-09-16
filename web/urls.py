from django.urls import path

from web import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.ProductListView.as_view(), name="products"),
    # path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
]
