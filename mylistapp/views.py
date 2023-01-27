from django.shortcuts import render
from django.views.generic import TemplateView
from .models import MyList
from django.contrib.auth.models import User
# Create your views here.


class MyListView(TemplateView):
    template_name = 'list.html'
    
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.POST.get('username'))
        print("o id é ", user.id)
        movies = MyList.objects.all().filter(user_id=user.id)
        print('OS FILMES SÃO:', movies[0].movie)
        
        
        
        return None
