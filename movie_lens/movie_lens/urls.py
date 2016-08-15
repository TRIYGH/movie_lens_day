from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^movie_rate/', include('movie_rate.urls')),
    url(r'^admin/', admin.site.urls),
]
