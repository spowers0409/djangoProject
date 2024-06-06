from django.urls import path
from .views import MainPageView, ContactPageView, AboutPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('about/', AboutPageView.as_view(), name='about'),
]