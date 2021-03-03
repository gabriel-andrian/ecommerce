from django.urls import path
from .views import ProductView, TransactionView

urlpatterns = [
    path('transaction/', TransactionView.as_view()),
    path('product/', ProductView.as_view()),
]