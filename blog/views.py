from django.shortcuts import render
from .models import Article

def home(request):
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(title__icontains=query)
    else:
        articles = Article.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'articles': articles})
