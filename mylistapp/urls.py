from django.urls import path
from .views import MyListView, deleteitem, updateitem

urlpatterns = [
    path('mylist/', MyListView.as_view(), name='mylist'),
    path("updateitem/<int:pk>", updateitem, name="updateitem"),
    path('deleteitem/<int:pk>', deleteitem, name='deleteitem'),
]
