from django.shortcuts import render
from django.core.paginator import Paginator

from admin_dashboard.models import Gallery
from admin_dashboard.models import Blog
from admin_dashboard.models import Event
from django.shortcuts import render, redirect
from django.contrib import messages
from admin_dashboard.forms import ContactForm
from admin_dashboard.models import Service



def home(request):
    services = Service.objects.all()[:3]  # Fetch top 6 services
    blogs = Blog.objects.all().order_by('-created_at')[:3]  # Fetch 5 latest blogs
    events = Event.objects.all().order_by('-date')[:3]  # Fetch 5 recent events
    images = Gallery.objects.all()[:4]  # Fetch 8 gallery images

    return render(request, 'index.html', {
        'services': services,
        'blogs': blogs,
        'events': events,
        'images': images,
    })

def about(request):
    return render(request, 'about.html')

def service_list(request):
    services = Service.objects.all().order_by('-created_at')
    return render(request, 'service_list.html', {'services': services})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your inquiry has been submitted. We will get back to you soon!")
            return redirect('contact_us')  # Redirect to prevent resubmission on page refresh
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def event_list(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'event_list.html', {'events': events})

# Create your views here.
# def home(request):
#     return render (request, 'index.html')
    



def gallery_view(request):
    images = Gallery.objects.all().order_by('-created_at')  # Fetch all images
    return render(request, 'gallery.html', {'images': images})




def blog_list(request):
    # Get all blogs ordered by the creation date
    all_blogs = Blog.objects.all().order_by('-created_at')

    # Featured blog (first blog in the queryset)
    featured_blog = Blog.objects.first()

    # Set up pagination (6 blogs per page)
    paginator = Paginator(all_blogs, 4)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    return render(request, 'blog_list.html', {
        'blogs': blogs,
        'featured_blog': featured_blog,
    })

def blog_detail(request, pk):
    # Get a single blog post by its primary key (pk)
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})

