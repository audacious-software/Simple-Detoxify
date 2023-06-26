import django

from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', django.contrib.admin.site.urls),
    url(r'^detoxify/', include('simple_detoxify.urls')),
]
