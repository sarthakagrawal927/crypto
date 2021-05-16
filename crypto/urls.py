
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prices/', views.prices, name='prices'),

    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
]
