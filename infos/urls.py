from django.urls import path
from .views import main, bio, contact

urlpatterns = [
    path('', main),
    path('bio/', bio),
    path('contact/', contact)
]