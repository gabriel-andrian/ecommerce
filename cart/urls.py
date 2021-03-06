from django.urls import path
from .views import CartView, CartItemView

urlpatterns = [
    path('cart/', CartView.as_view()),
    path('cart/item/<slug:slug>/', CartItemView.as_view())
]
