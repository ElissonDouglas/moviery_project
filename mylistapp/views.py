from django.shortcuts import render
from django.views.generic import TemplateView
from .models import MyList
from django.contrib.auth.models import User

import requests
from home.views import get_movie_data_by_id
# Create your views here.


MY_API_KEY = '7c5b4f0aacc314306fd23c1b4c621810'





class MyListView(TemplateView):
    template_name = 'list.html'
    
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.POST.get('username'))
        movies = MyList.objects.all().filter(user_id=user.id)
        
        all_movies = []
        
        for movie in movies:
            aux = get_movie_data_by_id(movie.movie)
            all_movies.append(aux)
        
        context = {
            'movies': all_movies,
        }
        
        return render(request, self.template_name, context)
