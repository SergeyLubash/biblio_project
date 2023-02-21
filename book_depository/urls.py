from django.contrib import admin
from django.urls import path, include

from bibliotek.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bibliotek/', include(router.urls)),
]


