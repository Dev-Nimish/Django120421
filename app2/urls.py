from django.urls import path
from app2 import views

app_name = "app2"

urlpatterns = [
    path('<pagename>', views.index, name="index"),
    path('page2/<email>/<location>', views.page2, name="page2"),
]
