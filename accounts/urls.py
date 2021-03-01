from django.urls import path
from .views import AccountView # LoginView, ProtectedView

urlpatterns = [
    path('accounts/', AccountView.as_view()),
    # path('login/', LoginView.as_view()),
    # path('protected/', ProtectedView.as_view())
]