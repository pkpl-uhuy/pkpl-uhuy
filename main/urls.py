from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.home, name='home'),

    # Auth
    path('login/', views.login_page, name='login'),
    #path('logout/', views.logout_view, name='logout'), soon yh

    # Member Only
    #path('edit/', views.edit, name='edit'), ini kalo viewnya udah dibuat
    #path('save/', views.save, name='save'), 
]