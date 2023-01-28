from django.shortcuts import render
from django.views.generic import TemplateView
from .models import MyList


import requests
from home.views import get_movie_data_by_id
# Create your views here.


MY_API_KEY = '7c5b4f0aacc314306fd23c1b4c621810'





class MyListView(TemplateView):
    template_name = 'list.html'
    
    
    def get(self, request, *args, **kwargs):
        movies = MyList.objects.filter(user_id=request.user.id).order_by('-id')
        all_movies = []
        
        for movie in movies:
            aux = get_movie_data_by_id(movie.movie)
            all_movies.append(aux)
        
        context = {
            'movies': all_movies,
        }
        
        return render(request, 'list.html', context)