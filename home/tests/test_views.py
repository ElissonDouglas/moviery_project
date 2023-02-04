from django.test import RequestFactory, TestCase, Client
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.models import User
import requests

from home.views import HomeView, MovieView, logout, LoginView, get_movie_data_by_id, get_recommended_movie_by_id, RegisterView
from mylistapp.views import additem, MyListView, updateitem, deleteitem
from mylistapp.models import MyList
from searchpage.views import search_movies, SearchView


class TestGetMovieDataById(TestCase):
    
    def setUp(self) -> None:
        self.response = 466
    
    
    def test_get_movie_data_by_id(self):
        movie_id = 466
        response = get_movie_data_by_id(movie_id)
        
        self.assertEqual(response['id'], self.response)
        
        
class TestGetRecommendedMovieById(TestCase):
    
    def setUp(self) -> None:
        self.response = 120268
    
    
    def test_get_recommended_movie_by_id(self):
        movie_id = 466
        response = get_recommended_movie_by_id(movie_id)
        
        self.assertEqual(response[0]['id'], self.response)   
  
  
class TestHomeView(TestCase):
    
    
    def setUp(self):
        self.factory = RequestFactory()
        self.view = HomeView.as_view()

    def test_get_context_data(self):
        request = self.factory.get('/')
        response = self.view(request)
        response.render()
        context = response.context_data

        self.assertIn('popular_movies', context)
        self.assertIn('top_rated_movies', context)
        

class TestMovieView(TestCase):
    
    def setUp(self):
        self.movie = 466
        self.client = Client()
        self.factory = RequestFactory()
        self.view = MovieView.as_view()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(self.user)
        
    def test_get_context_data(self):
        
        
        response = self.client.get('/movie/466')
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie.html', 'base.html')
        
        
        
class TestErro404View(TestCase):
    
    def test_erro_404_view(self):
        url = reverse('error404')
        cliente = Client()
        response = cliente.get('url')
        
        self.assertEqual(response.status_code, 404)
        
        self.assertTemplateUsed(response, '404.html')
        

class TestLogoutUser(TestCase):
    
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(self.user)

    def test_logout_user(self):
        
        # Log out the user
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')


class TestLoginView(TestCase):
    
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )

    def test_login_view_with_valid_credentials(self):
        response = self.client.get('/login/', {'username': 'testuser', 'password': 'password'})
        self.assertRedirects(response, '/')

    def test_login_view_with_invalid_credentials(self):
        response = self.client.get('/login/', {'username': 'testuser', 'password': 'incorrect'})
        self.assertIn('messages', response.context)
        
        

class TestRegisterView(TestCase):
    
    
    def setUp(self):
        self.client = Client()
    
    def test_get(self):
        request = self.client.get('/register/')
        
        self.assertTemplateUsed(request, 'registerpage.html')
        self.assertEquals(request.status_code, 200)
    

    def test_register_view(self):

        response = self.client.post(reverse('register'), data={
            'username': 'testuser',
            'fname': 'Test',
            'lname': 'User',
            'email': 'testuser@example.com',
            'password': 'secretpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_view_with_invalid_credentials(self):
        User.objects.create_user(username='test2user', password='test2user')
        response = self.client.post(reverse('register'), data={
            'username': 'test2user',
            'fname': 'Test',
            'lname': 'User',
            'email': '235f',
            'password': 'secretpassword',
        }) 
        
        self.assertEqual(response.status_code, 200)   


class TestMyListView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='userlist', password='passwordsecret')
        self.client.force_login(self.user)
        self.maxDiff = None
        

    def test_my_list_view(self):
        MyList.objects.create(user_id=self.user.id, movie=466)
        MyList.objects.create(user_id=self.user.id, movie=467, watched=True)
        
        all_movies = []
        
        for movie in MyList.objects.filter(user_id=self.user.id).order_by('-id'):
            aux = get_movie_data_by_id(movie.movie)
            if movie.watched:
                aux['watched'] = True
            else:
                aux['watched'] = False
            all_movies.append(aux)
        
        request = self.client.get(reverse('mylist'))
        
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'list.html')
        self.assertEqual(all_movies[0]['id'], 467)
        self.assertEqual(all_movies[0]['watched'], True)


class TestUpdateItem(TestCase):
    
    
    def setUp(self):
        self.client = Client()
        # create a user and log them in
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        # create a movie in MyList
        self.movie = MyList.objects.create(movie=466, user_id=self.user.id)

    def test_updateitem(self):
        response = self.client.post(reverse('updateitem', kwargs={'pk': self.movie.movie}))
        self.assertEqual(response.status_code, 302)
        updated_movie = MyList.objects.get(movie=self.movie.movie, user_id=self.user.id)
        self.assertTrue(updated_movie.watched)
        
    
class TestDeleteItem(TestCase):
    
    def setUp(self) -> None:
        self.client = Client()
        # create a user and log them in
        self.user = User.objects.create_user(username='testuser123', password='password')
        self.client.login(username='testuser123', password='password')
        # create a movie in MyList
        self.movie = MyList.objects.create(movie=466, user_id=self.user.id)
    
    
    def test_delete_item(self):
        response = self.client.post(reverse('deleteitem', kwargs={'pk': self.movie.movie}))
        
        self.assertEqual(response.status_code, 302)
        
        
        deleteditem = MyList.objects.filter(movie=466, user_id=self.user.id).exists()
        
        self.assertFalse(deleteditem)
        
        
class TestAddItem(TestCase):
    
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(username='j8aj8ajha', password='akda3535fd')
    
        
        
        
    def test_add_item(self):
        self.client.force_login(self.user)
        request = self.client.post(reverse('additem', kwargs={'pk': 466}))
        
        self.assertEqual(request.status_code, 302)
        
        request = self.client.post(reverse('additem', kwargs={'pk': 466}))
        self.assertTemplateUsed(request, 'list.html')
        

class TestSearchMovies(TestCase):
    
    def setUp(self) -> None:
        pass
    
    
    def test_search_movies(self):
        title = 'the avengers'
        title2 = '896u483u6##'
        
        results = search_movies(title=title)
        results2 = search_movies(title=title2)
        
        self.assertEqual(results[0]['id'], 299536)
        self.assertEqual(results2, 0)
        
        
class TestSearchView(TestCase):
    
    def setUp(self) -> None:
        self.client = Client()
    
    
    def test_search_view(self):
        request = self.client.post(reverse('search'), {'searchbar': 'shrek'})
        
        
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'search.html')



    
        

