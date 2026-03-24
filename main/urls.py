from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.home, name='home'),

    # Auth
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Member Only
    path('edit/', views.edit, name='edit'), 
    path('save/', views.save, name='save'), 
]