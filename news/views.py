from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, UpdateView,CreateView, DeleteView

from . import forms
from django.shortcuts import render, get_object_or_404

from news.models import NewsModel, CategoryModel


def news_list(request):
    news_data = NewsModel.objects.filter(status=NewsModel.Status.Published)
    context = {
        'news_data': news_data
    }

    return render(request, 'news_list.html', context)



def homepageview(request):
    news_list = NewsModel.objects.filter(status=NewsModel.Status.Published).order_by('-publish_time')[:3]
    home_list = NewsModel.objects.filter(status=NewsModel.Status.Published).order_by('-publish_time')[3:7]
    categories = CategoryModel.objects.all()
    context = {
        'news_list': news_list,
        'home_list': home_list,
        'categories': categories
    }
    return render(request, 'news/index.html', context)


class HomePageView(ListView):
    model = NewsModel
    template_name = 'news/index.html'
    context_object_name = 'news_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = NewsModel.objects.filter(status=NewsModel.Status.Published).order_by('-publish_time')[:3]
        context['home_list'] = NewsModel.objects.filter(status=NewsModel.Status.Published).order_by('-publish_time')[3:7]
        context['categories'] = CategoryModel.objects.all()
        return context

def contactpageview(request):
    form = forms.ContactForm(request.POST or None)
    print(request.POST)
    if request.method =='POST' and form.is_valid():
            form.save()
            return HttpResponse('<p>xabaringiz yuborildi</p>')
    context = {
        "form": form,
    }

    return render(request, 'news/contact.html',context)


def categorypageview(request):
    context = {}
    return render(request, 'news/category.html',context)

def newsdetailview(request, news):
    news = get_object_or_404(NewsModel,slug=news, status=NewsModel.Status.Published)
    context = {
        'news': news,
    }
    return render(request, 'news/single.html', context)



class LocalPageView(ListView):
    model = NewsModel
    template_name = 'news/mahalliy.html'
    context_object_name = 'local_list'

    def get_queryset(self):
        news =NewsModel.objects.filter(status=NewsModel.Status.Published, category__name='Mahalliy')
        return news


class WorldPageView(ListView):
    model = NewsModel
    template_name = 'news/jahon.html'
    context_object_name = 'world_list'

    def get_queryset(self):
        news =NewsModel.objects.filter(status=NewsModel.Status.Published, category__name='Jahon')
        return news

class FanTexnikaPageView(ListView):
    model = NewsModel
    template_name = 'news/fantexnika.html'
    context_object_name = 'fantexnika'

    def get_queryset(self):
        news =NewsModel.objects.filter(status=NewsModel.Status.Published, category__name='Fan-Texnika')
        return news

class SportPageView(ListView):
    model = NewsModel
    template_name = 'news/sport.html'
    context_object_name = 'sport_list'

    def get_queryset(self):
        news =NewsModel.objects.filter(status=NewsModel.Status.Published, category__name='Sport')
        return news


class NewsUpdateView(UpdateView):
    model = NewsModel
    fields = ('title', 'body','image','category','status')
    template_name = 'crud/update.html'
    success_url = reverse_lazy('home_page')

class NewsDeleteView(DeleteView):
    model = NewsModel
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('home_page')


class NewsCreateView(CreateView):
    model = NewsModel
    fields = ('title','slug', 'body','image','category','status')
    template_name = 'crud/create.html'
