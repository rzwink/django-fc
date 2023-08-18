from django.urls import include
from django.urls import path

from web import views

urlpatterns = [
    path("", views.index, name="index"),
    path("schedule/<str:pk>/", views.schedule, name="schedule"),
    path("products/", views.ProductListView.as_view(), name="products"),
    path("captcha/", include("captcha.urls")),
    # path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
]
