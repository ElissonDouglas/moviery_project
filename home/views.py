from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from mylistapp.models import MyList


import requests
from datetime import datetime

MY_API_KEY = '7c5b4f0aacc314306fd23c1b4c621810'

# https://api.themoviedb.org/3/movie/latest?api_key=<<api_key>>&language=en-US
def get_movies_data(option):
    
    response = requests.get(f'https://api.themoviedb.org/3/movie/{option}?api_key={MY_API_KEY}&language=en-US&page=1')
    data = response.json()
    all_data = data['results']
    
    return all_data


def get_movie_data_by_id(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={MY_API_KEY}&language=en-US')
    data = response.json()
    return data


def get_recommended_movie_by_id(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={MY_API_KEY}&language=en-US&page=1')
    data = response.json()
    return data['results']


class HomeView(TemplateView):
    template_name = 'home.html'
    popular_movies_data = get_movies_data('popular')
    top_rated_movies_data = get_movies_data('top_rated')
    
    def get_context_data(self,  **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['popular_movies'] = self.popular_movies_data
        context['top_rated_movies'] = self.top_rated_movies_data
        
        return context

    

class MovieView(TemplateView):
    template_name = 'movie.html'
   

    def get_context_data(self, movie_id, **kwargs):
        movie_data = get_movie_data_by_id(movie_id)
        recommended_movie = get_recommended_movie_by_id(movie_id)
        
        is_in_list = MyList.objects.filter(movie=movie_id, user_id=self.request.user.id).exists()
        
        
        context = {
            'movie': movie_data,
            'recommended': recommended_movie,
            'is_in_list': is_in_list,      
            }
        return context
 
 
    
    
    

class Erro404View(TemplateView):
    template_name = '404.html'
    

class RegisterView(TemplateView):
    template_name = 'registerpage.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
    
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
            messages.error(request, f'Username "{username}" has already been taken.')
            return render(request, self.template_name, {})
        except User.DoesNotExist:
            new_user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            new_user.save()
            return redirect('login')


class LoginView(TemplateView):
    template_name = 'login.html'
    
    
    
    
    
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        password = request.GET.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            
            return render(request, self.template_name, {'messages':messages.error(request, 'Invalid username or password')})

      
def logout_user(request):
    logout(request)
    return redirect('home')
    

class AboutView(TemplateView):
    template_name = 'about.html'
    