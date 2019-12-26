from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bob.urls')),
    path('', include('accounts.urls')),
    path('', include('problems.urls')),
    path('', include('django.contrib.auth.urls')),
]
