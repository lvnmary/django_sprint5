from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """Выводит посты на главную."""
    template = 'blog/index.html'
    post_list = 
    context = {'post_list': post_list}
    return render(request, template, context)

def post_detal(request, id):
    """Выводит пост на отдельную страницу."""
    template = 'blog/detail.html'
    post = 
    context = {'post': post}
    return render(request, template, context)

def category_posts(request, category_slug):
    """Выводит страницу категории."""
    template = 'blog/category.html'
    category = 
    post_list = 
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
