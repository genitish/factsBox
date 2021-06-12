from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .forms import NewsForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def news(request):
    form = NewsForm(request.POST)
    if form.is_valid():
        form.save()
        form = NewsForm()
    return render(request, 'news.html', {'form':form})