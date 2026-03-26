from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('tampilan/edit/', views.update_tampilan, name='update_tampilan'),
    path('profil/edit/<int:id>/', views.update_biodata, name='update_profil'),
]