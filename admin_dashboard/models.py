from django.db import models
from datetime import time
# Create your models here.python manage.py makemigrations


class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='logos/', blank=True, null=True, help_text="Upload the site logo")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Site Settings"


class Service(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the service")
    description = models.TextField(help_text="Detailed description of the service")
    image = models.ImageField(upload_to='services/', blank=True, null=True, help_text="Service image")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    job_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100, default='')  # Provide a default for non-nullable field
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True, default='')
    company_name = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=50, default='')
    job_title = models.CharField(max_length=100, default='')
    job_details = models.TextField(blank=True, null=True)  # Removed max_length, as it doesn't apply to TextField
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.company_name}"



class Event(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the event")
    description = models.TextField(help_text="Event description")
    image = models.ImageField(upload_to='events/', blank=True, null=True, help_text="Event image (optional)")
    location = models.CharField(max_length=200, help_text="Event location", default="Unknown Location")
    date = models.DateField(help_text="Date of the event")
    time = models.TimeField(help_text="Time of the event", default=time(12, 0))  # Default time set to 12:00 PM
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    
class Blog(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the blog")
    content = models.TextField(help_text="Blog content")
    image = models.ImageField(upload_to='blogs/', blank=True, null=True, help_text="Optional cover image")
    author = models.CharField(max_length=100, help_text="Author name", default="Admin")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Gallery(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the image")
    image = models.ImageField(upload_to='gallery/', help_text="Upload an image")
    description = models.TextField(blank=True, help_text="Optional description")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
