from django.urls import path
from .views import ListCreateProductView

# http://127.0.0.1:8000/api/v1/account
urlpatterns = [
    path("list_or_create/", ListCreateProductView.as_view()),
    


]
