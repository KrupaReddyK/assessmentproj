from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('Register')
        self.login_url = reverse('Login')
        self.home_url = reverse('home')
        self.create_url = reverse('tweetcreate')
        self.update_url = reverse('tweetupdate')
        self.delete_url = reverse('tweetdelete')
        self.user={
            'username':'uname',
            'password':'password',
            'password2':'password',
        }
        self.user_shortpassword={
             'username':'uname',
            'password':'pass',
            'password2':'pass',
        }
        self.user_unmatchingpassword={
             'username':'uname',
            'password':'pass',
            'password2':'pass1',
        }
        return super().setUp()
    
class RegisterTest(BaseTest):
    def test_viewPageCorrectly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'proj1/register.html')
        
    def test_registerUser(self):
        response = self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)
        
    def test_cantregisterUser_ShortPassword(self):
        response = self.client.post(self.register_url,self.user_shortpassword,format='text/html')
        self.assertEqual(response.status_code,400)
        
    def test_cantregisterUser_unmatchedPassword(self):
        response = self.client.post(self.register_url,self.user_unmatchingpassword,format='text/html')
        self.assertEqual(response.status_code,400)
        

class LoginTest(BaseTest):
    def test_viewPageCorrectly(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'proj1/login.html')
        
    def test_loginSuccess(self):
        response = self.client.post(self.register_url,self.user,format='text/html')
        user=User.objects.filter(username = self.user['username']).first()
        user.is_active=True
        user.save()
        response = self.client.post(self.login_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)
    
    def test_loginFail(self):
        response = self.client.post(self.register_url,self.user,format='text/html')
        user=User.objects.filter(username = self.user['username']).first()
        user.is_active=True
        user.save()
        response = self.client.post(self.login_url,self.user_unmatchingpassword,format='text/html')
        self.assertEqual(response.status_code,302)
    
        
class TweetTest(BaseTest):
    def test_viewHomePageCorrectly(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'proj1/home.html')
        
    def test_viewCreatePageCorrectly(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'proj1/tweet_form.html')
        
    def test_viewUpdatePageCorrectly(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'proj1/tweet_form.html')
        
    def test_viewDeletePageCorrectly(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'proj1/tweet_confirm_delete.html')

    
        
