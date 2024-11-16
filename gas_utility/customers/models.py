from django.contrib.auth.models import AbstractUser
from django.db import models
from gas_utility import settings

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  
    is_representative = models.BooleanField(default=True)  

    username = None  # Remove the username field
    USERNAME_FIELD = 'email'  # Use email as the unique identifier
    REQUIRED_FIELDS = ['name']  # Fields required when creating a superuser

    def __str__(self):
        role = "Customer" if self.is_representative else "Customer Support Representative"
        return f"{self.email} ({role})"


class ServiceRequest(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Link to the custom User model
        on_delete=models.CASCADE,
        related_name='service_requests'
    )
    request_subject = models.CharField(max_length=100)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")
    resolved_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.request_type} - {self.status}"