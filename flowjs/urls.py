from django.conf.urls import url
from .views import UploadView, CheckStateView


# JSON REQUESTS
urlpatterns = [
    url(r'^upload/$', UploadView.as_view()),
    url(r'^state/$', CheckStateView.as_view()),
]
