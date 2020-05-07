from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # upload multiple files by normal form without models
    path('', views.MultiUploadView.as_view(), name='multi_upload'),
]
