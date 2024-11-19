from django.contrib import admin
from .models import EmergencyIncident, EmergencyResponse

@admin.register(EmergencyIncident)
class EmergencyIncidentAdmin(admin.ModelAdmin):
    list_display = ('emergency_type', 'reporter', 'status', 'created_at')
    list_filter = ('emergency_type', 'status')
    search_fields = ('description', 'reporter__username')

@admin.register(EmergencyResponse)
class EmergencyResponseAdmin(admin.ModelAdmin):
    list_display = ('incident', 'responder', 'responded_at')
    list_filter = ('responded_at',)
    search_fields = ('response_details', 'responder__username')