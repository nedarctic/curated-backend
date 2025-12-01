from rest_framework import serializers
from .models import SubscriptionEmail, Message, Booking

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionEmail
        fields = ('id', 'email')
        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'message', 'email', 'name', 'travel_dates', 'phone')
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'email', 'full_name', 'phone', 'travel_date', 'special_requests', 'custom_destination_name', 'created_at')