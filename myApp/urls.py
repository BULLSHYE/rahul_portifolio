from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('header/', views.header_view, name='header'),
    path('footer/', views.footer_view, name='footer'),
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='service'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('blog/', views.blog_view, name='blog'),
    path('contact/', views.contact_view, name='contact'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)