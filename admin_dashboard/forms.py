from django import forms
from .models import Gallery
from .models import Blog
from .models import Event
from .models import Contact
from .models import Service
from django.contrib.auth.forms import PasswordChangeForm
from .models import SiteSettings

class LogoUploadForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = ['logo']


class AdminPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'image']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name', 'email', 'phone', 'company_name',
            'country', 'job_title', 'job_details'

        ]


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'image', 'location', 'date', 'time']


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'image', 'description']



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'author']
