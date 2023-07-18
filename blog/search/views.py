from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SearchForm
#from blog.news.models import Artiles

def search(request):
    search = request.GET.get("search", "нет")
    #news = Artiles.objects.order_by('-date')
    return render(request, 'search/search.html', context={'search': search, 'news': news})

def search2(request):
    search_form = SearchForm
    searchstr = request.GET.get("search", "undifined")
    return HttpResponse(f"<h2>Поисковый запрос: {searchstr}</h2>")