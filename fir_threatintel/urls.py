from django.urls import re_path

from fir_threatintel import views

app_name='fir_threatintel'

urlpatterns = [
    re_path(r'^update_api', views.update_api, name='update_api'),
]
