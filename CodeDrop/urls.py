from django.urls import path
from . import views

urlpatterns = [
    path('', views.create, name='index'),
    path('<str:unique_id>/', views.view_code, name='view_code'),
]
