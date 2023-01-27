from django.urls import path, include
from .views import SearchView

urlpatterns = [
    path('search/', SearchView.as_view(), name='search'),
    path('movie/<int:movie_id>', include('home.urls'), name='movie'),
]
