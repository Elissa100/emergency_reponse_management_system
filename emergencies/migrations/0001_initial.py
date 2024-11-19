# Generated by Django 5.1.3 on 2024-11-18 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyIncident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emergency_type', models.CharField(choices=[('MEDICAL', 'Medical Emergency'), ('FIRE', 'Fire'), ('ACCIDENT', 'Accident'), ('CRIME', 'Criminal Activity'), ('NATURAL_DISASTER', 'Natural Disaster')], max_length=20)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('REPORTED', 'Reported'), ('IN_PROGRESS', 'In Progress'), ('RESOLVED', 'Resolved'), ('CLOSED', 'Closed')], default='REPORTED', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_details', models.TextField()),
                ('responded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]