from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import EmergencyIncident, EmergencyResponse
from .forms import EmergencyReportForm, EmergencyResponseForm

@login_required
def emergency_list(request):
    """View all emergencies based on user role"""
    if request.user.user_type == 'ADMIN':
        emergencies = EmergencyIncident.objects.all().order_by('-created_at')
    elif request.user.user_type == 'RESPONDER':
        emergencies = EmergencyIncident.objects.filter(status__in=['REPORTED', 'IN_PROGRESS'])
    else:
        emergencies = EmergencyIncident.objects.filter(reporter=request.user)
    
    return render(request, 'emergencies/emergency_list.html', {'emergencies': emergencies})

@login_required
def emergency_detail(request, incident_id):
    """View details of specific emergency"""
    incident = get_object_or_404(EmergencyIncident, id=incident_id)
    responses = incident.responses.all().order_by('-responded_at')
    return render(request, 'emergencies/emergency_detail.html', {
        'incident': incident,
        'responses': responses
    })

@login_required
def report_emergency(request):
    """Report new emergency"""
    if request.method == 'POST':
        form = EmergencyReportForm(request.POST)
        if form.is_valid():
            emergency = form.save(commit=False)
            emergency.reporter = request.user
            emergency.save()
            messages.success(request, 'Emergency reported successfully!')
            return redirect('emergency_detail', incident_id=emergency.id)
    else:
        form = EmergencyReportForm()
    
    return render(request, 'emergencies/report_emergency.html', {'form': form})

@login_required
@login_required
def respond_emergency(request, incident_id):
    """Respond to an emergency"""
    if request.user.user_type != 'RESPONDER':
        messages.error(request, 'Only responders can respond to emergencies.')
        return redirect('emergency_list')
    
    incident = get_object_or_404(EmergencyIncident, id=incident_id)
    
    if request.method == 'POST':
        form = EmergencyResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.incident = incident
            response.responder = request.user
            response.save()
            
            # Update incident status to 'IN_PROGRESS' or as required
            incident.status = 'IN_PROGRESS'
            incident.save()

            messages.success(request, 'Your response has been recorded.')
            return redirect('emergency_detail', incident_id=incident.id)
    else:
        form = EmergencyResponseForm()

    return render(request, 'emergencies/respond_emergency.html', {
        'form': form,
        'incident': incident
    })

@login_required
def update_emergency_status(request, incident_id):
    """Update emergency status"""
    if request.user.user_type not in ['ADMIN', 'RESPONDER']:
        messages.error(request, 'You do not have permission to update emergency status.')
        return redirect('emergency_list')
    
    incident = get_object_or_404(EmergencyIncident, id=incident_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['REPORTED', 'IN_PROGRESS', 'RESOLVED', 'CLOSED']:
            incident.status = new_status
            incident.save()
            messages.success(request, 'Emergency status updated successfully!')
        else:
            messages.error(request, 'Invalid status provided.')
    
    return redirect('emergency_detail', incident_id=incident.id)

def respond_emergency_list(request):
    """View all responses to emergencies"""
    if request.user.user_type == 'ADMIN':
        responses = EmergencyResponse.objects.all().order_by('-responded_at')
    elif request.user.user_type == 'RESPONDER':
        responses = EmergencyResponse.objects.filter(responder=request.user)
    else:
        responses = EmergencyResponse.objects.filter(incident__reporter=request.user)
    
    return render(request, 'emergencies/respond_emergency_list.html', {'responses': responses})

@login_required
def respond_emergency_detail(request, response_id):
    """View details of specific response"""
    response = get_object_or_404(EmergencyResponse, id=response_id)
    return render(request, 'emergencies/respond_emergency_detail.html', {'response': response})

