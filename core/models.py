from django.db import models

class SubscriptionEmail(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email
    
class Message(models.Model):
    message = models.TextField()
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.message} from {self.email}"
    
class Booking(models.Model):
    email = models.EmailField()
    destination = models.TextField()
    fromDate = models.DateTimeField()
    toDate = models.DateTimeField()
    customDestination = models.TextField(null=True)
    
    def __str__(self):
        return f"{self.email} made a booking!"