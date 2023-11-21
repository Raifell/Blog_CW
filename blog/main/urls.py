from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('post/<slug:post_slug>/', views.post_page, name='post_page'),
    path('add/', views.add_post_page, name='add_page'),
    path('edit/<slug:edit_slug>', views.edit_post_page, name='edit_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
