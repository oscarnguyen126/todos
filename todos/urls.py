from django.urls import path
from . import views

urlpatterns = [
    path('', views.listtodo),
    path('<int:id>/', views.detailtodo),
]
