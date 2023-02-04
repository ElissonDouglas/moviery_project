from django.urls import path
from .views import MyListView, deleteitem, updateitem, additem

urlpatterns = [
    path('mylist', MyListView.as_view(), name='mylist'),
    path('additem/<int:pk>', additem, name='additem'),
    path("updateitem/<int:pk>", updateitem, name="updateitem"),
    path('deleteitem/<int:pk>', deleteitem, name='deleteitem'),
]
