from django.urls import path
from .views import MyListView

urlpatterns = [
    path('mylist/', MyListView.as_view(), name='mylist'),
]
