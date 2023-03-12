from django.contrib import admin
from django.urls import path

# Home view
from home.views import (
    home_screen_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view),
]
