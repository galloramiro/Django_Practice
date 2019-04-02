from django.urls import path
from .views import QuoteFormView, QuoteView

urlpatterns = [
    path('', QuoteFormView.as_view(), name='home'),
    path('quotes/', QuoteView.as_view(), name='quotes'),
]