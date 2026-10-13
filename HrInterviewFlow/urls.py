from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),
    path('candidate-auth/', views.candidate_auth, name='candidate_auth'),
    path('hr-auth/', views.hr_auth, name='hr_auth'),
    path('instructions/', views.instructions, name='instructions'),
    path('interview/', views.interview, name='interview'),
    path('admin-dashboard/', views.admin_page, name='admin_page'),
]