from django.urls import path
from .views import QuoteFormView, QuoteListView

urlpatterns = [
    path('', QuoteFormView.as_view(), name='home'),
    path('quotes/', QuoteListView.as_view(), name='quotes-list'),
]