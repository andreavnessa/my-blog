
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("myapp/", include("myapp.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

]
