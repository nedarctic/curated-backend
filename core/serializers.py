from rest_framework import serializers
from .models import SubscriptionEmail, Message, Booking

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionEmail
        fields = ('id', 'email')
        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'message', 'email')
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'email', 'fromDate', 'toDate', 'destination', 'customDestination')