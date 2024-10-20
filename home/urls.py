from django.urls import path
from . import views

urlpatterns = [
    path('', views.StaffListAPIView.as_view(), name='staff_list_api'),
    path('entry/', views.EntryApiView.as_view(), name='entry_api'),
    path('exit/', views.ExitAPIView.as_view(), name='exit_api'),
]