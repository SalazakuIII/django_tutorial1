from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_method),
    path('another_method', views.another_method),
    path('redirected_method', views.redirected_method)
]