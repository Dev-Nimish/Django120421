from django.urls import path
from app1 import views

app_name = "app1"

urlpatterns = [
    path('', views.index, name="app1-index"),
    path('page2/', views.page2, name="app1-page2"),
]
