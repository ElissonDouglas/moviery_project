from django.urls import path, include
from .views import HomeView, MovieView, Erro404View, RegisterView, LoginView, logout_user
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('movie/<int:movie_id>', MovieView.as_view(), name='movie'),
    path('404/', Erro404View.as_view(), name='error404'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
