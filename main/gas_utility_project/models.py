from django.db import models
from django.contrib.auth.models import User
import string
import random
import uuid
def generate_unique_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))
class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'), 
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved')
    ]
    user = models.CharField(max_length=40)
    request_type = models.CharField(max_length=100)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    resolution_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
