from django.urls import path
from . import views

urlpatterns = [
    path('bears', views.one_method),
    path('bears/<int:my_val>', views.another_method),
    path('bears/<str:name>/poke', views.yet_another_method),
    path('<int:id>/<str:color>', views.one_more_method)
]