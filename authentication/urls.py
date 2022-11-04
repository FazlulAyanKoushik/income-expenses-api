from django.urls import path
from .views import RagistrationView

urlpatterns = [
    path('register', RagistrationView.as_view(), name='register')
]