from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

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

def list_posts(request):
    return render(request, 'feed.html', {'posts': posts}) 
    # content = []
    # for post in posts:
    #     content.append(
    #         f"""<h1>{post['name']}</h1>
    #         <p>{post['user']} - {post['timestamp']}</p>
    #         <figure><img src="{post['picture']}"/></figure>"""
    #     ) 
    # return HttpResponse('<br>'.join(content))


