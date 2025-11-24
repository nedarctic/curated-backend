from rest_framework import generics
from .models import SubscriptionEmail, Message, Booking
from .serializers import SubscriptionSerializer, MessageSerializer, BookingSerializer

class BookingView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    
class MessageView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    
class SubscribeView(generics.ListCreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = SubscriptionEmail.objects.all()
    