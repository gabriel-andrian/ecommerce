from django.urls import path
from .views import ProductView, TransactionView

urlpatterns = [
    path('transaction/', TransactionView.as_view()),
    path('product/', ProductView.as_view()),
    path("<slug:slug>/", ProductView.as_view(), name="detail"),
    path("category/<slug:slug>/", ProductView.as_view(), name="list_by_category")
]