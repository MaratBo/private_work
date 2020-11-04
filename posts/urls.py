from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.post_group),
]
