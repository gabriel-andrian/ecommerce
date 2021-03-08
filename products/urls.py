from django.urls import path
from .views import ProductView, TransactionView, CategoriesView

urlpatterns = [
    path('transaction/', TransactionView.as_view()),
    path('product/', ProductView.as_view()),
    path('product/<slug:slug>/', ProductView.as_view()),
    path('category/', CategoriesView.as_view()),
    path('category/<slug:slug>/', CategoriesView.as_view())
]
