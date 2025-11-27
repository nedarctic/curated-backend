from django.contrib import admin

from .models import Booking, Message, SubscriptionEmail

admin.site.register(Booking)
admin.site.register(Message)
admin.site.register(SubscriptionEmail)
