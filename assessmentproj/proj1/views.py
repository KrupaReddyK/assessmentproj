from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import tweet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def register(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    else:
        form = UserCreationForm()
    return render(request, 'proj1/register.html', {'form':form})



@login_required
def home(request):
    context = {'tweets':tweet.objects.all()}
    return render(request,'proj1/home.html',context)
 
@login_required   
def profile(request):
    return render(request, 'proj1/profile.html') 
    context = {'tweets': tweet.objects.all}
    
class TweetListView(LoginRequiredMixin,ListView):
    model = tweet
    template_name = 'proj1/home.html'
    ordering = ['-datetime']
    
    
class TweetCreateView(LoginRequiredMixin,CreateView):
    model = tweet
    fields = ['text']
    
    success_url = '/home'
    
    def form_valid(self,form):
        form.instance.uname = self.request.user
        return super().form_valid(form)

class TweetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = tweet
    
    fields = ['text']
    success_url = '/home'
    
    
    
    def test_func(self):
        tweet = self.get_object()
        if(self.request.user == tweet.uname):
            return True
        return False
    
class TweetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = tweet
    
    
    success_url = '/home'
    
    
    
    def test_func(self):
        tweet = self.get_object()
        if(self.request.user == tweet.uname):
            return True
        return False
    
    
    