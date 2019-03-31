from django.urls import path
from .views import HomePageView, AboutListlView, ContactPageView, AboutUpdate

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutListlView.as_view(), name='about-list'),
    path('about/update/<int:pk>/', AboutUpdate.as_view(), name='update'),
    path('contact/', ContactPageView.as_view(), name='contacto'),
]