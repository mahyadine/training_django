from django.shortcuts import render

# Create your views here.
def index(request):
    posts = [
        {'id' : 1, 'title': 'First Post','body' : 'This is my first post' },
        {'id' : 2, 'title': 'Second Post','body' : 'This is my second post'},
        {'id' : 3, 'title': 'Third Post','body' : 'This is my third post'},
    ]
    return render(request, 'blog/index.html', {'posts' : posts})
