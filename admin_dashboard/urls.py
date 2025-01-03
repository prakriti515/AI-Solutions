from django.urls import path

from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    # Login Page
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # path('create-event/', views.create_event, name='create_event'),
    # path('create-blog/', views.create_blog, name='create_blog'),
    path('admin-gallery/', views.admin_gallery, name='admin_gallery'),
    path('logout/', views.logout_view, name='logout'),
    # path('gallery/', views.admin_gallery, name='admin_gallery'),
    path('gallery/add/', views.add_gallery_item, name='add_gallery_item'),
    path('gallery/edit/<int:pk>/', views.edit_gallery_item, name='edit_gallery_item'),
    path('gallery/delete/<int:pk>/', views.delete_gallery_item, name='delete_gallery_item'),
    path('admin-blogs/', views.admin_blog, name='admin_blog'),
    path('blogs/add/', views.add_blog, name='add_blog'),
    path('blogs/edit/<int:pk>/', views.edit_blog, name='edit_blog'),
    path('blogs/delete/<int:pk>/', views.delete_blog, name='delete_blog'),
    path('admin-events/', views.admin_event, name='admin_event'),
    path('events/add/', views.add_event, name='add_event'),
    path('events/edit/<int:pk>/', views.edit_event, name='edit_event'),
    path('events/delete/<int:pk>/', views.delete_event, name='delete_event'),
    path('admin-contacts/', views.manage_contacts, name='manage_contacts'),
    path('contacts/update/<int:pk>/', views.update_contact_status, name='update_contact_status'),
    path('admin-services/', views.manage_services, name='manage_services'),
    path('services/add/', views.add_service, name='add_service'),
    path('services/edit/<int:pk>/', views.edit_service, name='edit_service'),
    path('services/delete/<int:pk>/', views.delete_service, name='delete_service'),
    path('change-password/', views.change_password, name='change_password'),
    path('logo/', views.manage_logo, name='manage_logo'),
     path('logo/remove/', views.remove_logo, name='remove_logo'),
]



