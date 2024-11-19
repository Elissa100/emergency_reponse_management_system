from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import EmergencyIncident, EmergencyResponse
from users.models import CustomUser

@receiver(post_save, sender=EmergencyIncident)
def notify_responders(sender, instance, created, **kwargs):
    if created:
        # Notify responders matching the emergency type
        responders = CustomUser.objects.filter(user_type='RESPONDER')
        for responder in responders:
            # In a real system, implement actual notification mechanism
            print(f"Notifying {responder.username} about new emergency")

@receiver(post_save, sender=EmergencyResponse)
def notify_reporter(sender, instance, created, **kwargs):
    if created:
        # Notify the original reporter about the response
        reporter = instance.incident.reporter
        # In a real system, implement actual notification mechanism
        print(f"Notifying {reporter.username} about emergency response")