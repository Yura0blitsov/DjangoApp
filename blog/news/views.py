from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.db import connection
# Create your views here.
def news_home2(request):
    search = request.GET.get("search", "")
    if search == "":
        news = Artiles.objects.order_by('-date')
    else:
        news = Artiles.objects.filter(title__icontains=search)
    return render(request, 'news/news_home.html', {'news': news, 'search': search})
def news_home(request):
    search = request.GET.get("search", "")
    if search == "":
        news = Artiles.objects.order_by('-date')
    else:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM news_artiles WHERE title = '{search}' OR anons = '{search}' OR full_text = '{search}'")
            newss = cursor.fetchone()
            print(newss)
            if newss != None:
                newst = Artiles()
                newst.id = newss[0]
                newst.title = newss[1]
                newst.anons = newss[2]
                newst.full_text = newss[3]
                newst.date = newss[4]
                news = [newst]
            else:
                news = []
    return render(request, 'news/news_home.html', {'news': news, 'search': search})
    #return HttpResponse(f"<h1> {news.anons} {news.title}</h1>")

class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Artiles
    template_name = 'news/create.html'
    form_class = ArtilesForm

class NewsDeleteView(DeleteView):
    model = Artiles
    success_url = '/news/'
    template_name = 'news/news-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.current_user = request.user
            post.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ArtilesForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)