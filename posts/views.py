from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm

posts = [
    {
        "name": "pepe",
        "age": "24",
        "timestamp": datetime.now().strftime('%Y %b %dth - %H:%M hrs'),
        "picture": 'https://robohash.org/1'
    },
    {
        "name": "juan",
        "age": "27",
        "timestamp": datetime.now().strftime('%Y %b %dth - %H:%M hrs'),
        "picture": 'https://robohash.org/2'
    },
    {
        "name": "lucia",
        "age": "21",
        "timestamp": datetime.now().strftime('%Y %b %dth - %H:%M hrs'),
        "picture": 'https://robohash.org/3'
    }
]

@login_required
def list_posts(request):
    return render(request, 'posts/feed.html', {'posts': posts}) 

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(
        request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }     
    )



