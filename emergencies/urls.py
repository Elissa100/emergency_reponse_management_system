from django.urls import path
from . import views

urlpatterns = [
    path('', views.emergency_list, name='emergency_list'),
    path('report/', views.report_emergency, name='report_emergency'),
    path('<int:incident_id>/', views.emergency_detail, name='emergency_detail'),
    path('<int:incident_id>/respond/', views.respond_emergency, name='respond_emergency'),
    path('<int:incident_id>/update/', views.update_emergency_status, name='update_emergency_status'),
    path('respond/', views.respond_emergency_list, name='respond_emergency_list'),
    path('respond/<int:response_id>/', views.respond_emergency_detail, name='respond_emergency_detail'),
]