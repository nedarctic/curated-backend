from django.urls import path
from .views import SubscribeView, MessageView, BookingView

urlpatterns = [
    path('subscribe/', SubscribeView.as_view()),
    path('book/', BookingView.as_view()),
    path('message/', MessageView.as_view()),
]