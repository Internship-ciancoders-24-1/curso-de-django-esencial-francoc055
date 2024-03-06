from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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



