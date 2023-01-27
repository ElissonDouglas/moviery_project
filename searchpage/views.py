from django.views.generic import TemplateView
from django.shortcuts import render

import requests

# Create your views here.
MY_API_KEY = '7c5b4f0aacc314306fd23c1b4c621810'


def search_movies(title):
    title = title.split(' ')
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={MY_API_KEY}&query={"+".join(title)}')
    data = response.json()
    all_results = data['results']
    if len(all_results) == 0:
        return 0
    else:
        sorted_results = sorted(all_results, key=lambda x: x['popularity'], reverse=True)
        return sorted_results


class SearchView(TemplateView):
    template_name = 'search.html'
    
    def post(self, request, *args, **kwargs):
        title = request.POST.get('searchbar')
        
        context = {
            'results': search_movies(title)
        }
        
        return render(request, 'search.html', context)
    
