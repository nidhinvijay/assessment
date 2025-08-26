# mypollsite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line connects to the poll/urls.py file we just edited
    path('', include('poll.urls')),
]