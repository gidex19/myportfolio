from django.urls import path
from . import views as my_app_view

urlpatterns = [
    path('', my_app_view.home, name='homepage'),
    # path('download/', my_app_view.download, name='download'),
]
