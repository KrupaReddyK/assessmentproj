from django.contrib import admin
from django.urls import path, include
from .import views
from .views import TweetListView, TweetCreateView,TweetUpdateView, TweetDeleteView

urlpatterns = [
    path('', views.register, name='Register'),
    path('home/', TweetListView.as_view(), name='home'),
    path('create/', TweetCreateView.as_view(), name='tweetcreate'),
    path('tweet/<int:pk>/update/', TweetUpdateView.as_view(), name='tweetupdate'),
    path('tweet/<int:pk>/delete/', TweetDeleteView.as_view(), name='tweetdelete'),
    
    
]