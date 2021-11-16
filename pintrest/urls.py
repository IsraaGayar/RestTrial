from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('adin/', admin.site.urls),
    path('', include('api.v1.urls'))

]
