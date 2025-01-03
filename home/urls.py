from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('contact',views.contact_us, name='contact_us'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('events/', views.event_list, name='event_list'),
    path('services/', views.service_list, name='service_list'),
    path('about/', views.about, name='about'),
]