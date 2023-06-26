from django.conf.urls import url

from .views import simple_detoxify_score

urlpatterns = [
    url(r'^score$', simple_detoxify_score, name='simple_detoxify_score'),
]
