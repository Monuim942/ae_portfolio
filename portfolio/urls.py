# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # المسار الرئيسي للبورتفوليو المرتبط بالدالة التي عدلناها
    path('', views.contact_view, name='projects_list'), 
]