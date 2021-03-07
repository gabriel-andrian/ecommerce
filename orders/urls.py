from django.urls import path
from .views import OrderView

urlpatterns = [
    path('order/', OrderView.as_view())
]
