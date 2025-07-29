# feedback_project/urls.py
from django.contrib import admin
from django.urls import path, include
from feedback.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/', include('feedback.urls')),  # Feedback app URLs

    # Add this line for the root URL
    path('', home, name='home'),  # Root URL maps to the home view
]
