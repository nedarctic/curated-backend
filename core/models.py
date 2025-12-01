from django.db import models

class SubscriptionEmail(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email
    
class Message(models.Model):
    message = models.TextField()
    email = models.EmailField()
    name = models.TextField(null=True)
    travel_dates = models.TextField(null=True)
    phone = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return f"{self.message} from {self.email}"
    
class Booking(models.Model):
    full_name = models.CharField(max_length=255, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True)
    travel_date = models.DateField(null=True)
    special_requests = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    custom_destination_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Booking from {self.full_name} ({self.email})"
