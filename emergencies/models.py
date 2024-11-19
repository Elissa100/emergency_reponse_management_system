from django.db import models
from django.conf import settings

class EmergencyIncident(models.Model):
    EMERGENCY_TYPES = [
        ('MEDICAL', 'Medical Emergency'),
        ('FIRE', 'Fire'),
        ('ACCIDENT', 'Accident'),
        ('CRIME', 'Criminal Activity'),
        ('NATURAL_DISASTER', 'Natural Disaster')
    ]

    STATUS_CHOICES = [
        ('REPORTED', 'Reported'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed')
    ]

    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, 
                               on_delete=models.CASCADE, 
                               related_name='reported_emergencies')
    emergency_type = models.CharField(max_length=20, choices=EMERGENCY_TYPES)
    description = models.TextField()
    status = models.CharField(max_length=20, 
                            choices=STATUS_CHOICES, 
                            default='REPORTED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_emergency_type_display()} - {self.status}"

class EmergencyResponse(models.Model):
    incident = models.ForeignKey(EmergencyIncident, 
                               on_delete=models.CASCADE,
                               related_name='responses')
    responder = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='emergency_responses')
    response_details = models.TextField()
    responded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to {self.incident} by {self.responder.username}"