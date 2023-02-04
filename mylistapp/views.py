from django.shortcuts import render, redirect
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
            if movie.watched:
                aux['watched'] = True
            else: 
                aux['watched'] = False
            all_movies.append(aux)
        
        context = {
            'movies': all_movies,
        }
        
        return render(request, 'list.html', context)
  
  
def updateitem(request, pk):
    movie = MyList.objects.get(movie=pk, user_id=request.user.id)
    movie.watched = True
    movie.save()
    return redirect('mylist')
  
    
def deleteitem(request, pk):
    movie = MyList.objects.get(movie=pk, user_id=request.user.id)
    movie.delete()
    return redirect('mylist')


def additem(request, pk):
    if request.method == 'POST':
        user = request.user
        movie = pk #request.POST.get('movie_id')
        if not MyList.objects.filter(user=user, movie=movie).exists():
            form = MyList(user=user, movie=movie)
            form.save()
            return redirect('mylist')
        else:
            return render(request, 'list.html')