from django.shortcuts import render
from .models import ContactInquiry, Event, Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Gallery

from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Gallery
from .forms import GalleryForm  # We'll create this form next.

from .models import Blog
from .forms import BlogForm  # We'll create this form next.

from .models import Event
from .forms import EventForm  # We'll create this form next.
from .models import Contact
from .models import Service
from .forms import ServiceForm  # We'll create this form next.

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AdminPasswordChangeForm
from django.views.decorators.csrf import csrf_exempt
from .models import SiteSettings
from .forms import LogoUploadForm

from admin_dashboard.models import Contact, Event, Blog
@login_required
def admin_dashboard(request):
    inquiries_count = Contact.objects.count()
    resolved_count = Contact.objects.filter(status='Resolved').count()
    pending_count = Contact.objects.filter(status='Pending').count()
    events_count = Event.objects.count()
    blogs_count = Blog.objects.count()

    return render(request, 'dashboard/admin_dashboard.html', {
        'inquiries_count': inquiries_count,
        'resolved_count': resolved_count,
        'pending_count': pending_count,
        'events_count': events_count,
        'blogs_count': blogs_count,
    })


def manage_logo(request):
    site_settings = SiteSettings.objects.first()
    if request.method == 'POST':
        form = LogoUploadForm(request.POST, request.FILES, instance=site_settings)
        if form.is_valid():
            form.save()
            messages.success(request, "Logo updated successfully!")
            return redirect('manage_logo')
        else:
            messages.error(request, "Error updating the logo. Please try again.")
    else:
        form = LogoUploadForm(instance=site_settings)

    return render(request, 'dashboard/manage_logo.html', {'form': form, 'site_settings': site_settings})



@csrf_exempt
def remove_logo(request):
    site_settings = SiteSettings.objects.first()
    if site_settings and site_settings.logo:
        site_settings.logo.delete()  # Delete the logo file
        site_settings.logo = None
        site_settings.save()
        messages.success(request, "Logo removed successfully!")
    else:
        messages.error(request, "No logo to remove.")
    return redirect('manage_logo')


def change_password(request):
    if request.method == 'POST':
        form = AdminPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keeps the user logged in after password change
            messages.success(request, "Your password was successfully updated!")
            return redirect('admin_dashboard')  # Redirect to the dashboard or desired page
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = AdminPasswordChangeForm(user=request.user)
    return render(request, 'dashboard/change_password.html', {'form': form})


def manage_services(request):
    services = Service.objects.all().order_by('-created_at')
    return render(request, 'dashboard/manage_services.html', {'services': services})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Service added successfully!")
            return redirect('manage_services')
    else:
        form = ServiceForm()
    return render(request, 'dashboard/add_service.html', {'form': form})

def edit_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, "Service updated successfully!")
            return redirect('manage_services')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'dashboard/edit_service.html', {'form': form, 'service': service})

def delete_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    messages.success(request, "Service deleted successfully!")
    return redirect('manage_services')



def manage_contacts(request):
    contacts = Contact.objects.exclude(name="Anonymous").exclude(email="Not Provided")
    return render(request, 'dashboard/manage_contacts.html', {'contacts': contacts})

def update_contact_status(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.status = 'Resolved' if contact.status == 'Pending' else 'Pending'
    contact.save()
    return redirect('manage_contacts')


# Event Management View
def admin_event(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'dashboard/admin_event.html', {'events': events})

# Add Event View
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Event added successfully!")
            return redirect('admin_event')
    else:
        form = EventForm()
    return render(request, 'dashboard/add_event.html', {'form': form})

# Edit Event View
def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfully!")
            return redirect('admin_event')
    else:
        form = EventForm(instance=event)
    return render(request, 'dashboard/edit_event.html', {'form': form, 'event': event})

# Delete Event View
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    messages.success(request, "Event deleted successfully!")
    return redirect('admin_event')



# def admin_gallery(request):
#     images = Gallery.objects.all()
#     return render(request, 'dashboard/admin_gallery.html', {'images': images})

def logout_view(request):
    logout(request)
    return redirect('login')



# Admin Gallery View
def admin_gallery(request):
    images = Gallery.objects.all()
    return render(request, 'dashboard/admin_gallery.html', {'images': images})

# Add Gallery Item
def add_gallery_item(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Image added successfully!")
            return redirect('admin_gallery')
    else:
        form = GalleryForm()
    return render(request, 'dashboard/add_gallery_item.html', {'form': form})

# Edit Gallery Item
def edit_gallery_item(request, pk):
    image = get_object_or_404(Gallery, pk=pk)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, "Image updated successfully!")
            return redirect('admin_gallery')
    else:
        form = GalleryForm(instance=image)
    return render(request, 'dashboard/edit_gallery_item.html', {'form': form, 'image': image})


def delete_gallery_item(request, pk):
    image = get_object_or_404(Gallery, pk=pk)
    if request.method == 'POST':
        image.delete()
        messages.success(request, "Image deleted successfully!")
        return redirect('admin_gallery')
    return render(request, 'dashboard/delete_gallery_item.html', {'image': image})



# Blog Management View
def admin_blog(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'dashboard/admin_blog.html', {'blogs': blogs})

# Add Blog View
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog added successfully!")
            return redirect('admin_blog')
    else:
        form = BlogForm()
    return render(request, 'dashboard/add_blog.html', {'form': form})

# Edit Blog View
def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog updated successfully!")
            return redirect('admin_blog')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'dashboard/edit_blog.html', {'form': form, 'blog': blog})

# Delete Blog View
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    messages.success(request, "Blog deleted successfully!")
    return redirect('admin_blog')
